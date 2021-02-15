from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import numpy as np
from pockets import drawFloor, drawScianki, drawCircle
from balls import balls, dd
from siły import *

# licznik czasu - do wymuszenia częstotliwości odświeżania
tick = 0
eye = np.array([-5., 5., 10.])  # pozycja
orient = np.array([0., 0., -1.])  # kierunek
up = np.array([0., 1., 0.])  # góra


whiteBall = {}
whiteBall = dd(whiteBall)
whiteBall.v = [0, 0, 0]
whiteBall.p = whiteBall.p = [0, 0.6, 7.5]
whiteBall.m = 10
whiteBall.r = 0.4
whiteBall.col = [1, 1, 1]
whiteBall.quad = gluNewQuadric()

# rysowanie sfery
def drawSphere(part):
    glLoadIdentity()
    glTranslatef(part.p[0], part.p[1], part.p[2])
    glColor3fv(part.col)
    gluSphere(part.quad, part.r, 16, 16)


# współczynniki
s = 0.76
rot_cam = 90
cam_r = 6
w_aero = 0.47
g = -9.7


# ruch sfery
def updateSphere(part, dt, aero, graw, tarc):
    # opór areodynamiczny
    part.v[0] -= aero[0]
    part.v[2] -= aero[2]

    # opór areodynamiczny
    part.v[0] -= tarc[0]
    part.v[2] -= tarc[1]

    # siły grawitacji
    #part.v[1] += graw

    part.p[0] += dt * part.v[0]
    part.p[2] += dt * part.v[2]

def checkSphereToSciankiCollision(part):
    global s
    if not checkPockets(part):
        if part.p[0] - part.r < 5:
            pass
        else:
            part.p[0] = 5 + part.r
            part.v[0] = -part.v[0] * s

        if part.p[0] + part.r > -5:
            pass
        else:
            part.p[0] = -part.r - 5
            part.v[0] = -part.v[0] * s

        if part.p[2] - part.r < 11:
            pass
        else:
            part.p[2] = 11 + part.r
            part.v[2] = - part.v[2] * s

        if part.p[2] + part.r > -11:
            pass
        else:
            part.p[2] = -part.r - 11
            part.v[2] = - part.v[2]



# obsługa kolizji

#czy należy do powierzchni łuzy
def checkPockets(part):
    px = part.p[0]
    py = part.p[2]
    #pierwsza łuza
    if -4.55 >= px and -10.9 >= py:
        return True
    # druga łuza
    if px <= -5.75 and -1.2 < py <= 1.2:
        return True
    #trzecia łuza
    if -4.55 <= px and 10.9 <= py:
        return True
    #czwarta łuza
    if 4.55 <= px and py >= 10.9:
        return True
    #piąta łuza
    if px >= 5.75 and -1.2 < py <= 1.2:
        return True
    #szósta łuza
    if 5.75 >= px and py <= -10.9:
        return True
    return False

#z podłogą
def updateSphereCollision(part):
    if checkPockets(part):
        pass
        #for i in range(10):
            #part.p[1] += graw(part, g)

#kula z kulą
def checkSphereToSphereCollision(part1, part2):
    global s

    # odległośc między środkami
    d = sqrt((part1.p[0] - part2.p[0])**2 + (part1.p[1] - part2.p[1])**2 + (part1.p[2] - part2.p[2])**2)
    if d <= part1.r + part2.r:
        #obsługa 'glitcha'
        if d < part1.r + part2.r:
            w = np.array([part2.p[0]-part1.p[0], part2.p[2]-part1.p[2]])
            depth = part1.r + part2.r - d
            w_unit = w / (w**2).sum()**0.5
            w_unit *= depth/2
            part2.p[0] += w_unit[0]
            part2.p[2] += w_unit[1]
            part1.p[0] += -w_unit[0]
            part1.p[2] += -w_unit[1]

        #transformacja dp X' Y'
        dx = abs(part1.p[0] - part2.p[0])
        dy = abs(part1.p[2] - part2.p[2])
        alpha = atan2(dy, dx)

        v1 = np.matmul([[cos(alpha), sin(alpha)], [-sin(alpha), cos(alpha)]], [part1.v[0], part1.v[2]])
        v2 = np.matmul(np.array([[cos(alpha), sin(alpha)], [-sin(alpha), cos(alpha)]]), [part2.v[0], part2.v[2]])

        v1final = ((part1.m - part2.m) * v1[0] + 2*part2.m*v2[0])/(part1.m + part2.m)
        v2final = ((part2.m - part1.m) * v2[0] + 2*part1.m*v1[0])/(part1.m + part2.m)

        v1_inv = np.matmul([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]], [v1final, v1[1]])
        v2_inv = np.matmul([[cos(alpha), -sin(alpha)], [sin(alpha), cos(alpha)]], [v2final, v2[1]])

        part1.v[0] = v1_inv[0]
        part1.v[2] = v1_inv[1]
        part2.v[0] = v2_inv[0]
        part2.v[2] = v2_inv[1]


def cupdate():
    global tick
    ltime = time.time()
    if ltime < tick + 0.1:  # max 10 ramek / s
        return False
    tick = ltime
    return True

def keyboard(bkey, x, y):
    key = bkey.decode("utf-8")
    global s, rot_cam, cam_r
    if key == 'k':
        s += 0.05
    if key == 'l':
        s -= 0.05
    if key == "e":
        cam_r -= 1
    if key == "q":
        cam_r += 1
    if key == 'd':
        rot_cam += 5
    if key == 'a':
        rot_cam -= 5
    if key == 'y':
        whiteBall.v[2] -= 35


def display():
    if not cupdate():
        return
    global s, rot_cam, cam_r, aero, g
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 100)
    camx = sin(np.radians(rot_cam)) * cam_r
    camz = cos(np.radians(rot_cam)) * cam_r
    gluLookAt(camx, 15, camz, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    drawScianki()
    drawFloor()
    drawCircle()
    drawSphere(whiteBall)
    checkSphereToSciankiCollision(whiteBall)
    updateSphere(whiteBall, 0.1, aero(whiteBall, w_aero), graw(whiteBall, g), tarc(whiteBall))
    for ball in balls:
        checkSphereToSphereCollision(whiteBall, ball)
    for ball in balls:
        checkSphereToSciankiCollision(ball)
        updateSphereCollision(ball)
        updateSphere(ball, 0.1, aero(ball, w_aero), graw(ball, g), tarc(ball))
        drawSphere(ball)
        for ball1 in balls:
            if ball.p[0] != ball1.p[0] or ball.p[1] != ball1.p[1] or ball.p[2] != ball1.p[2]:
                checkSphereToSphereCollision(ball, ball1)


    glutKeyboardFunc(keyboard)
    glFlush()


glutInit()
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Bilard")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutDisplayFunc(display)
glutIdleFunc(display)
glClearColor(1.0, 1.0, 1.0, 1.0)
glClearDepth(1.0)


glDepthFunc(GL_LESS)
glEnable(GL_DEPTH_TEST)
# przygotowanie oświetlenia
glEnable(GL_LIGHT0)
glLight(GL_LIGHT0, GL_POSITION, [0., 5., 5., 0.])
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
# przygotowanie sfery
gluQuadricNormals(whiteBall.quad, GLU_SMOOTH)
for ball in balls:
    gluQuadricNormals(ball.quad, GLU_SMOOTH)
glutMainLoop()
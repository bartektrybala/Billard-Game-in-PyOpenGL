from OpenGL.GL import *
from math import *

# rysowanie podłogi
def drawFloor():
    glLoadIdentity()
    glColor3fv([0.0, 1.0, 0.0])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)

    glVertex3fv([-6.35, 0, -12.7])
    glVertex3fv([-6.35, 0, 12.7])
    glVertex3fv([6.35, 0, 12.7])
    glVertex3fv([6.35, 0, -12.7])
    glEnd()

def drawScianki():
    #scianki wewnątrz
    glLoadIdentity()  # jedno sciano
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([-5.75, 0, -10.9])
    glVertex3fv([-5.75, 0.6, -10.9])
    glVertex3fv([-5.75, 0.6, -1.2])
    glVertex3fv([-5.75, 0, -1.2])
    glEnd()

    glLoadIdentity()  # drugo sciano
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([-5.75, 0, 1.2])
    glVertex3fv([-5.75, 0.6, 1.2])
    glVertex3fv([-5.75, 0.6, 10.9])
    glVertex3fv([-5.75, 0, 10.9])
    glEnd()

    glLoadIdentity()  # trzecio sciano
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([-4.55, 0, 12.1])
    glVertex3fv([-4.55, 0.6, 12.1])
    glVertex3fv([4.55, 0.6, 12.1])
    glVertex3fv([4.55, 0, 12.1])
    glEnd()

    glLoadIdentity()  # czwarto sciano
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([5.75, 0, 10.9])
    glVertex3fv([5.75, 0.6, 10.9])
    glVertex3fv([5.75, 0.6, 1.2])
    glVertex3fv([5.75, 0, 1.2])
    glEnd()

    glLoadIdentity()  # piata
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([5.75, 0, -1.2])
    glVertex3fv([5.75, 0.6, -1.2])
    glVertex3fv([5.75, 0.6, -10.9])
    glVertex3fv([5.75, 0, -10.9])
    glEnd()

    glLoadIdentity()  # szosta
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([4.55, 0, -12.1])
    glVertex3fv([4.55, 0.6, -12.1])
    glVertex3fv([-4.55, 0.6, -12.1])
    glVertex3fv([-4.55, 0, -12.1])
    glEnd()

    #ścianki zewnętrzne
    glLoadIdentity()
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([-8.1, 0, -14.45])
    glVertex3fv([-8.1, 1, -14.45])
    glVertex3fv([-8.1, 1, 14.45])
    glVertex3fv([-8.1, 0, 14.45])
    glEnd()

    glLoadIdentity()
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([-8.1, 0, 14.45])
    glVertex3fv([-8.1, 1, 14.45])
    glVertex3fv([8.1, 1, 14.45])
    glVertex3fv([8.1, 0, 14.45])
    glEnd()

    glLoadIdentity()
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([8.1, 0, 14.45])
    glVertex3fv([8.1, 1, 14.45])
    glVertex3fv([8.1, 1, -14.45])
    glVertex3fv([8.1, 0, -14.45])
    glEnd()

    glLoadIdentity()
    glColor3fv([0.66, 0.27, 0.07])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex3fv([8.1, 0, -14.45])
    glVertex3fv([8.1, 1, -14.45])
    glVertex3fv([-8.1, 1, -14.45])
    glVertex3fv([-8.1, 0, -14.45])
    glEnd()

def drawCircle():
    r = 1
    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle)*r-6.35, 0.0, sin(angle)*r-12.7)
    glEnd()

    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle) * r - 6.35, 0.0, sin(angle) * r)
    glEnd()

    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle)*r-6.35, 0.0, sin(angle)*r+12.7)
    glEnd()

    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle)*r+6.35, 0.0, sin(angle)*r+12.7)
    glEnd()

    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle)*r+6.35, 0.0, sin(angle)*r)
    glEnd()

    glLoadIdentity()
    glColor3fv([0.37, 0.37, 0.37])
    glPolygonMode(GL_FRONT, GL_FILL)
    glBegin(GL_LINE_LOOP)
    for vertex in range(40):
        angle = float(vertex) * 2.0 * pi / 8
        glVertex3f(cos(angle)*r+6.35, 0.0, sin(angle)*r-12.7)
    glEnd()


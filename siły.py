from math import *

#współczynniki
S = pi
ps = 1.21
g = -9.81
u = 0.015       #współczynnik tarcia z tkaniną [0.005, 0.015

#siła grawitacji
def fg(x, g):
    return x + g

def runge(h, p, g):
    k1 = h * fg(p.v[1], g)
    k2 = h * (fg(p.v[1], g) + k1/2)
    k3 = h * (fg(p.v[1], g) + k2/2)
    k4 = h * (fg(p.v[1], g) + k3)
    return 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def graw(p, g):
    return runge(0.005, p, g)

# opór aerodynamiczny

def aero(p, w_aero):
    global ps, S
    b = w_aero * ps * S / 2
    x = rungex(0.02, f, p, b)
    y = rungey(0.02, f, p, b)
    z = rungez(0.02, f, p, b)
    vk = [x, y, z]
    return vk


def f(x, m, b):
    return x * exp(-b/m)


def rungex(h, f, p, b):
    k1 = h * f(p.v[0], p.m, b)
    k2 = h * f(p.v[0] + k1 / 2, p.m, b)
    k3 = h * f(p.v[0] + k2 / 2, p.m, b)
    k4 = h * f(p.v[0] + k3, p.m, b)
    return 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def rungey(h, f, p, b):
    k1 = h * f(p.v[1], p.m, b)
    k2 = h * f(p.v[1] + k1 / 2, p.m, b)
    k3 = h * f(p.v[1] + k2 / 2, p.m, b)
    k4 = h * f(p.v[1] + k3, p.m, b)
    return 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def rungez(h, f, p, b):
    k1 = h * f(p.v[2], p.m, b)
    k2 = h * f(p.v[2] + k1 / 2, p.m, b)
    k3 = h * f(p.v[2] + k2 / 2, p.m, b)
    k4 = h * f(p.v[2] + k3, p.m, b)
    return 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

#tarcie toczne
def ft(x):
    global g, u
    return x + g*u


def runget(h, p):
    k1 = h * ft(p)
    k2 = h * (ft(p) + k1/2)
    k3 = h * (ft(p) + k2/2)
    k4 = h * (ft(p) + k3)
    return 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def tarc(p):
    if p.v[0] > 0.2 and p.v[2] > 0.2:
        x = runget(0.01, p.v[0])
        y = runget(0.01, p.v[2])
    else:
        x = 0
        y = 0
    vt = [x, y]
    return vt


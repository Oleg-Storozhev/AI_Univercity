import math
import sympy

a = 2
b = 0.7
c = 1.3
d = 0.5
t1 = 0.90


def x(t):
    return a * math.sqrt(t + b)


def y(t):
    return t**c + d


def Trajectory(t):
    to = 0.5 * t
    tn = 1.5 * t
    ht = (tn-to)/20
    for i in range(20):
        ti = to+i*ht
        xi = x(ti)
        yi = y(ti)
        print("i =", i, "\nti =", ti, "\nxi =", xi, "\nyi =", yi)


Trajectory(t1)

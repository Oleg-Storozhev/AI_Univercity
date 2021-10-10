import math
import sys

import matplotlib.pyplot as plt

a = 2.06
b = 0.73
c = 1.32
d = 0.48
t1 = 1.59
x_all = []
y_all = []


def x(t):
    return a * math.sqrt(t + b)


def y(t):
    return t**c + d


def Trajectory(t):
    to = 0.5 * t
    tn = 1.5 * t
    ht = (tn-to)/20
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -sys.maxsize
    max_y = -sys.maxsize

    for i in range(20):
        ti = to + i*ht
        min_x = min(min_x, x(ti))
        min_y = min(min_y, y(ti))
        max_x = max(max_x, x(ti))
        max_y = max(max_y, y(ti))

    mash = 5/min((max_x-min_x), (max_y-min_y))

    for i in range(20):
        ti = to + i*ht
        xi = x(ti) * mash
        yi = y(ti) * mash
        x_all.append(xi)
        y_all.append(yi)
        print("i =", i, "\nti =", round(ti, 5), "\txi =", round(xi, 5), "\tyi =", round(yi, 5))

    plt.grid()
    plt.plot(x_all, y_all, 'b')
    plt.scatter(x(t1)*mash, y(t1)*mash, s=100, c='r')
    plt.arrow(x(t1)*mash, y(t1)*mash, 0, Vy(t1)*mash, width= 0.05, ec= 'black')
    plt.arrow(x(t1)*mash, y(t1)*mash, Vx(t1)*mash, 0, width= 0.05, ec= 'black')
    plt.arrow(x(t1)*mash, y(t1)*mash, Vx(t1)*mash, Vy(t1)*mash, width= 0.05, color= 'black')
    plt.show()

    plt.grid()
    plt.plot(x_all, y_all, 'b')
    plt.scatter(x(t1)*mash, y(t1)*mash, s=100, c='r')
    plt.arrow(x(t1)*mash, y(t1)*mash, 0, Wy(t1)*mash, width= 0.05, ec= 'blue')
    plt.arrow(x(t1)*mash, y(t1)*mash, Wx(t1)*mash, 0, width= 0.05, ec= 'blue')
    plt.arrow(x(t1)*mash, y(t1)*mash, Wx(t1)*mash, Wy(t1)*mash, width= 0.05, color= 'black')
    #plt.arrow(x(t1)*mash, y(t1)*mash, Wt(t1)*mash, Wn(t1)*mash, width= 0.05, color= 'black')
    plt.show()


def Vx(t):
    return a / (2 * math.sqrt(t + b))


def Vy(t):
    return c * t**(c-1)


def V(t):
    return math.sqrt(Vx(t)**2 + Vy(t)**2)


def Wx(t):
    return -a/(4*math.sqrt(t+b)*(t+b))


def Wy(t):
    return c * (c-1) * t**(c-2)


def W(t):
    return math.sqrt(Wx(t)**2 + Wy(t)**2)


def Wt(t):
    return (Vx(t) * Wx(t) + Vy(t) * Wy(t))/V(t)


def Wn(t):
    return math.sqrt(W(t)**2 - Wt(t)**2)


def ro(t):
    return V(t)**2/Wn(t)


Trajectory(t1)

print("\nti =", round(t1, 5),
      "\nКоордината xi =", round(x(t1), 5),
      "\nКоордината yi =", round(y(t1), 5),
      "\nСоставляющая Vx =", round(Vx(t1), 5),
      "\nСоставляющая Vy =", round(Vy(t1), 5),
      "\nМодуль скорости V =", round(V(t1), 5),
      "\nСоставляющая Wx =", round(Wx(t1), 5),
      "\nСоставляющая Wy =", round(Wy(t1), 5),
      "\nМодуль ускорения W =", round(W(t1), 5),
      "\nСоставляющая Wt =", round(Wt(t1), 5),
      "\nСоставляющая Wn =", round(Wn(t1), 5),
      "\nРадиус кривизны ro = ", round(ro(t1), 5)
      )

print(x_all, "\n", y_all)

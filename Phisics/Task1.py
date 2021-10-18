import math
import sys

import matplotlib.pyplot as plt

# Контрольный набор данных
a = 2.06
b = 0.73
c = 1.32
d = 0.48
t1 = 1.59

# Тестовый набор данных
# a = 2
# b = 0.7
# c = 1.3
# d = 0.5
# t1 = 0.9
x_all = []
y_all = []


def x(t):  # считаем x в точке t
    return a * math.sqrt(t + b)


def y(t):  # считаем y в точке t
    return t ** c + d


def Trajectory(t):  # считаем все точки траектории, включая точки M1
    to = 0.5 * t
    tn = 1.5 * t
    ht = (tn - to) / 20
    for i in range(20):
        ti = to + i * ht
        xi = x(ti)
        yi = y(ti)
        print("i =", i, "\nti =", round(ti, 5), "\txi =", round(xi, 5), "\tyi =", round(yi, 5))


def TrajectoryMash(t, m):  # считаем траекторию в указанном масштабе
    x_all.clear()
    y_all.clear()
    to = 0.5 * t
    tn = 1.5 * t
    ht = (tn - to) / 20
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -sys.maxsize
    max_y = -sys.maxsize

    for i in range(20):
        ti = to + i * ht
        min_x = min(min_x, x(ti))
        min_y = min(min_y, y(ti))
        max_x = max(max_x, x(ti))
        max_y = max(max_y, y(ti))

    mash = m / min((max_x - min_x), (max_y - min_y))

    print("\n\nTrajectory with mash", m)
    for i in range(20):
        ti = to + i * ht
        xi = x(ti) * mash
        yi = y(ti) * mash
        x_all.append(xi)
        y_all.append(yi)
        print("i =", i, "\nti =", round(ti, 5), "\txi =", round(xi, 5), "\tyi =", round(yi, 5))

    return mash


def DrawVxVy(t, m):  # рисуем вектора скорости Vx Vy |V|
    mash_vec = m / min(math.fabs(Vx(t)), math.fabs(Vy(t)))
    plt.grid()
    plt.plot(x_all, y_all, 'b')
    plt.scatter(x(t1) * mash, y(t1) * mash, s=100, c='r')
    plt.arrow(x(t1) * mash, y(t1) * mash, 0, Vy(t1) * mash_vec, width=0.05, ec='black')
    plt.arrow(x(t1) * mash, y(t1) * mash, Vx(t1) * mash_vec, 0, width=0.05, ec='black')
    plt.arrow(x(t1) * mash, y(t1) * mash, Vx(t1) * mash_vec, Vy(t1) * mash_vec, width=0.05, color='black')
    plt.show()
    print("\nVx with mash", Vx(t1) * mash_vec)
    print("Vy with mash", Vy(t1) * mash_vec)
    print("|V| with mash", V(t1) * mash_vec)


def DrawWxWyWtWn(t, m):  # рисуем вектора скорости Wx Wy Wt Wn |W|
    mash_vec = m / min(min(math.fabs(Wx(t)), math.fabs(Wy(t))), min(math.fabs(Wt(t)), math.fabs(Wn(t))))
    plt.grid()
    plt.plot(x_all, y_all, 'b')
    plt.scatter(x(t1) * mash, y(t1) * mash, s=100, c='r')
    plt.arrow(x(t1) * mash, y(t1) * mash, 0, Wy(t1) * mash_vec, width=0.05, ec='blue')
    plt.arrow(x(t1) * mash, y(t1) * mash, Wx(t1) * mash_vec, 0, width=0.05, ec='blue')
    plt.arrow(x(t1) * mash, y(t1) * mash, Wx(t1) * mash_vec, Wy(t1) * mash_vec, width=0.05, color='black')
    plt.arrow(x(t1) * mash, y(t1) * mash, (Vx(t1) * mash_vec) / (V(t1) * mash_vec * Wt(t1) * mash_vec) * 6, (Vy(t1) * mash_vec)/ (V(t) * mash_vec * Wt(t1) * mash_vec) *6,
              width=0.05, color='red')
    plt.arrow(x(t1) * mash, y(t1) * mash, -(Vy(t1) * mash_vec) / (V(t1) * mash_vec * Wn(t1) * mash_vec) * 6, (Vx(t1) * mash_vec) / (V(t) * mash_vec * Wn(t1) * mash_vec)*6,
              width=0.05, color='red')
    plt.show()
    print("\nWx with mash", Wx(t1) * mash_vec)
    print("Wy with mash", Vy(t1) * mash_vec)
    print("|W| with mash", W(t1) * mash_vec)
    print("Wt with mash", Wt(t1) * mash_vec)
    print("Wn with mash", Wn(t1) * mash_vec)


def Vx(t):  # находим вектор Vx
    return a / (2 * math.sqrt(t + b))


def Vy(t):  # находим вектор Vy
    return c * t ** (c - 1)


def V(t):  # находим точку |V|
    return math.sqrt(Vx(t) ** 2 + Vy(t) ** 2)


def Wx(t):  # находим точку Wx
    return -a / (4 * math.sqrt(t + b) * (t + b))


def Wy(t):  # находим вектор Wy
    return c * (c - 1) * t ** (c - 2)


def W(t):  # находим вектор |W|
    return math.sqrt(Wx(t) ** 2 + Wy(t) ** 2)


def Wt(t):  # находим вектор Wt
    return (Vx(t) * Wx(t) + Vy(t) * Wy(t)) / V(t)


def Wn(t):  # находим ветор Wn
    return math.sqrt(W(t) ** 2 - Wt(t) ** 2)


def ro(t):  # найдем радиус кривизны
    return V(t) ** 2 / Wn(t)


# Начало программы
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
mash = TrajectoryMash(t1, 5)
DrawVxVy(t1, 3)
DrawWxWyWtWn(t1, 1.5)

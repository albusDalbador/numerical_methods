import numpy as np 
from random import random
from math import *
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def func(t,omega):
    return sin(omega * t) + sin(2 * omega * T) + sin(3 * omega * T)


def generate_array_of_F_values(f,T,N,omega):
    points = []
    step = (T * 3) / N 
    t = 0.0
    while t <= T * 3 :
        points.append(f(t,omega))
        t += step
    return points

def generate_array_of_G_values(g,T,N,sigma):
    points = []
    step = (T * 3) / N 
    t = 0.0
    while t <= T * 3 :
        points.append(g(t,sigma))
        t += step
    return points


def h(t,omega):
    return random() - 0.5 + func(t,omega)

def g(t,sigma):
    return 1 / (sigma * sqrt(2 * pi)) * exp(- pow(t,2) / (2 * sigma ** 2))


def calculate_splot_product(f_k,g_k,g_k_inversed):
    f = []
    for i in range (len(f_k)):
        f.append(f_k[i] * (g_k[i] + g_k_inversed[i]))
    return f


def draw_function_with_noise(f,T,omega):
    x_points = []
    y_points = []
    t = 0.0
    while t <= T * 3:
        x_points.append(t)
        y_points.append(f(t,omega) + random() - 0.5)
        t += 0.01
    plt.plot(x_points,y_points)
    # plt.show()

def draw_function_with_given_y(y_points,T):
    pass





if __name__ == "__main__":
    k = 8
    N = 2 ** k
    T = 1.0
    omega = 2 * pi/ T
    sigma = 20/T
    t_max = T * 3
    dt = t_max / N


    f_t = generate_array_of_F_values(h,T,N,omega)
    g_t = generate_array_of_G_values(g,T,N,sigma)

    f_k = fft(f_t)
    g_k = fft(g_t)
    g_k_inversed = ifft(g_t)

    f = calculate_splot_product(f_k,g_k,g_k_inversed)

    f_smoothed = ifft(f)

    draw_function_with_noise(func,T,omega)

    real_parts = [item.real for item in f_smoothed]
    # plt.plot(np.arange(0.0,T*3 + 0.01,0.01),modules)

    normalized = [item*2.5/np.amax(real_parts) for item in real_parts]
    plt.plot(np.arange(0.0,T*3+0.01,(T * 3) / N),normalized)
    plt.show()

    # print(len(f_smoothed))

    plt.show()

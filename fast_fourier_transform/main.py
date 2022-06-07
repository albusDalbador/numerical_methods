import numpy as np
import matplotlib.pyplot as plt
from math import *
from random import random
from scipy.fft import fft, ifft


def f_0(t,omega):
    return sin(omega*t) + sin( 2 * omega * t) + sin(3 * omega * t)
#omega = 2pi/T - pulsacja


def f(t,omega):
    return f_0(omega,t) + random() - 0.5


def g(t,sigma):
    return 1/(sigma * sqrt(2 * pi)) * exp(-t**2/(2 * sigma**2))


def fill_f_0_array(f_0,omega,N,t_max):
    dt = t_max/N
    t = 0.0
    array = []
    while t <= t_max:
        array.extend([f_0(t,omega),0.0])
        t += dt
    return array


def fill_f_with_noise(f,omega,N,t_max):
    dt = t_max/N
    t = 0.0
    array = []
    while t <= t_max:
        array.extend([f(t,omega),0.0])
        t += dt
    return array


def fill_g_array(g,sigma,N,t_max):
    array = []
    t = 0.0
    dt = t_max/N
    while t <= t_max:
        array.extend([g(t,sigma),0.0])
        t += dt
    return array


def calculate_f_splot_transform(f_k,g_1_k,g_2_k):
    splot = []
    for i in range(len(f_k)):
        splot.append(f_k[i]*(g_1_k[i] + g_2_k[i]))
    return splot

def plot_result_function():
    pass

def plot_function_with_noise(f,omega,N,t_max):
    x_points = []
    y_points = []
    t = 0.0
    dt = t_max/N
    while t <= t_max:
        x_points.append(t)
        y_points.append(f(t,omega))
        t += dt
    plt.plot(x_points,y_points)
    plt.show()


def plot_smoothed_function(f_array,N,t_max):
    ind =0
    x = 0.0
    step = t_max/N
    x_points = []
    y_points = []
    while ind < len(f_array):
        x_points.append(ind)
        y_points.append(f_array[ind])
        x += step
        ind += 2
    plt.plot(x_points,y_points)
    plt.show()



if __name__ == "__main__":
    k = 8
    T = 1.0
    t_max = T*3
    sigma = T/20
    omega = 2*pi/T

    for k in (8,10,12):
        N = 2**k
        dt = t_max/N    

        plot_function_with_noise(f,omega,N,t_max)

        f_0_array = fill_f_0_array(f_0,omega,N,t_max)
        f_array = fill_f_with_noise(f,omega,N,t_max)
        g_1_array = fill_g_array(g,sigma,N,t_max)
        g_2_array = fill_g_array(g,sigma,N,t_max)

        f_k = fft(f_array)
        g_k_1 = fft(g_1_array)
        g_k_2 = np.fft.ifft(g_2_array)

        f_array = calculate_f_splot_transform(f_k,g_k_1,g_k_2)

        f_inverse = np.fft.ifft(f_array)

        plot_smoothed_function(f_inverse,N,t_max)




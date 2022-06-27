from http.client import ImproperConnectionState
from os import rename
from unittest.loader import VALID_MODULE_NAME
import matplotlib.pyplot as plt
from random import random
from math import *

from sympy import interpolating_spline


def generate_random_from_normal_distribution(mu,sigma):
    x_1 = random()
    x_2 = random()
    return sqrt(-2*log(x_1))*cos(2*pi*x_2)*sigma + mu

# def calculate_empiricial_probability_density(values,intervals,range):
#     x_points = []
#     y_values = [0]*intervals
#     y_points = []
#     N = len(values)
#     V_delta = range / intervals
#     step = N/intervals
#     while intervals > 0:
#         intervals -= 1
#         x_points.append(intervals*step)
#     for x in values:
#         y_values[floor(x/step)] += 1
#     for n in y_values:
#         y_points.append(n/N/V_delta)
#     return (x_points,y_points)

if __name__ == "__main__":
    T = 100
    u = 1.66*10**(-27)
    m = 40*u 
    k = 1.38*10**(-23)
    sigma = sqrt(k*T/m)
    
    for l in (3,4,5,6):
        N_l = 10**l

        V_values = []
        for i in range(0,N_l):
            V_1 = generate_random_from_normal_distribution(0,sigma)
            V_2 = generate_random_from_normal_distribution(0,sigma)
            V_3 = generate_random_from_normal_distribution(0,sigma)
            V_n = sqrt(V_1**2 + V_2**2 + V_3**2)

            V_values.append(V_n)
        (x_density,y_density) = calculate_empiricial_probability_density(V_values,30,5*sigma)

        plt.hist(V_values,bins=30,range=(0,5*sigma))
        plt.plot(x_density,y_density)
        plt.show()

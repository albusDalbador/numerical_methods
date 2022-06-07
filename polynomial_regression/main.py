from cmath import pi
from random import random
import numpy as np
import matplotlib.pylab as plt
from math import *
from pkg_resources import fixup_namespace_packages
import mpmath as mp
from pyparsing import delimited_list
# from decimal 


def func(x,x_min,x_max,x_zero,sigma):
    return sin((14*pi*x)/(x_max - x_min)) * (exp(-pow(x - x_zero,2)/(2 * sigma**2)) + exp(-pow(x+x_zero,2)/(2 * sigma**2)))



def C(x):
    return (random() - 0.5) / 5



def f_with_noise(x,x_min,x_max,x_zero,sigma):
    return func(x,x_min,x_max,x_zero,sigma) + C(x)



def draw_chart_of_function_with_noise(func,x_min,x_max,x_zero,sigma):
    x_points = []
    y_points = []
    x_current = x_min
    while x_current <= x_max:
        x_points.append(x_current)
        y_points.append(func(x_current,x_min,x_max,x_zero,sigma))
        x_current = round(x_current + 0.02,5)
    plt.plot(x_points,y_points)
    plt.show()



def generate_x_points(x_min,x_max,number_of_points):
    x_points = []
    for i in range (number_of_points+1):
        x_points.append(round(x_min + (x_max - x_min)/number_of_points*i,4))
    return x_points



def calc_y_points(func,x_points,x_zero,sigma):
    y_points = []
    for item in x_points:
        y_points.append(func(item,x_points[0],x_points[-1],x_zero,sigma))
    return y_points



def generate_q_array(x_points):
    q_array = []
    for item in x_points:
        q_array.append((item - x_points[0])/( (x_points[-1] - x_points[0]) /len(x_points)))
    return q_array



def calc_factor_polynomial(q,k):
    res = 1
    for i in range (k):
        res *= q - i
    return res


#from presenation (for randomly placed points)

def calc_alpha_j_plus_1(x_points,phi,j):
    delimeter = 0.0
    meter = 0.0
    for i in range (len(phi[j])):
        meter += x_points[i] * pow(phi[j][i],2)
        delimeter += pow(phi[j][i],2)
    return meter / delimeter



def calc_beta_j(x_points,phi,j):
    if j == 1:
        return 0
    else:
        meter = 0.0
        delimeter = 0.0
        for i in range(len(phi[j])):
            meter += x_points[i] * phi[j-1][i] * phi[j][i]
            delimeter += pow(phi[j-1][i],2)
        return meter / delimeter


# def generate_phi_matrix(x_points):
def generate_matrix_of_polynomials(x_points,m):
    phi = np.zeros((m+2,len(x_points)))
    phi[1] = np.full((1,len(x_points)),1)
    for j in range (1,m+1):
        # print(j)
        for i in range (len(x_points)):
            phi[j+1][i] = (x_points[i] - calc_alpha_j_plus_1(x_points,phi,j) * phi[j][i]) - calc_beta_j(x_points,phi,j) * phi[j-1][i]
    return phi



def C_k(y_points,phi,k):
    res = 0
    for i in range (len(phi[k])):
        res += y_points[i] * phi[k][i]
    return res


def S_k(phi,k):
    res = 0
    for i in range(len(phi[k])):
        res += phi[k][i] ** 2
    return res


def calc_approximation(phi,m,y_points):
    func_points = []
    for i in range (len(phi[0])):
        # func_points.append()
        tempPoint = 0
        for k in range (m):
            # if round(S_k(phi,k),6) > 0:
            tempPoint += (C_k(y_points,phi,k)/S_k(phi,k)) * phi[k][i]
        func_points.append(tempPoint)
    return func_points



if __name__ == "__main__":

    x_min = -4.0
    x_max = 4.0
    x_zero = 2.0
    sigma = (x_max - x_min) / 16
    num_of_nodes = 200
    m = 50

    x_points = generate_x_points(x_min,x_max,num_of_nodes)
    y_points = calc_y_points(f_with_noise,x_points,x_zero,sigma)
    phi = generate_matrix_of_polynomials(x_points,m)

    approximated_points = calc_approximation(phi,m,y_points)

    plt.plot(x_points,approximated_points)
    draw_chart_of_function_with_noise(f_with_noise,x_min,x_max,x_zero,sigma)


    x = generate_x_points(x_min,x_max,num_of_nodes)


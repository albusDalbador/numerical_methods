import numpy as np
from math import *
from scipy.special import roots_legendre, eval_legendre, roots_laguerre, roots_hermite
import matplotlib.pyplot as plt


def  c_1_a(x1,x2):
    a = 2
    c = 1
    return 1/(2*a**2)*log(a**2*x2**2+c**2) - 1/(2*a**2)*log(a**2*x1**2+c**2)

def c_2_a(k):
    return factorial(k)

def f_for_legendre_method(x):
    return x/(4*x**2 + 1)

def f_for_laguerre_method(x,k):
    return x**k
    
def f_for_gauss_hemite_method_x_part(x):
    return sin(x)**2

def f_for_gauss_hemite_method_y_part(y):
    return sin(y)**4

c_dok = 0.1919832644


def calc_integral_legendre_method(a,b,num_of_points,roots,weights,function):
    result = 0.0
    for k in range (0,num_of_points+2):
        result += weights[k]*function((a+b)/2 + (b-a)/2*roots[k])
    return (b-a)/2*result


def calc_integral_leguerre_method(num_of_points,roots,weights,function,power):
    result = 0.0
    for k in range (0,num_of_points+2):
        result += weights[k]*function(roots[k],power)
    return result


def calc_integral_hermite_method(num_of_points,roots, weights,function_x,function_y):
    resultX = 0.0
    resultY = 0.0
    for k in range (0,num_of_points + 2):
        resultX += weights[k]*function_x(roots[k])
        resultY += weights[k]*function_y(roots[k])
    return resultY * resultX




if __name__ == "__main__":
    
    # print("\ndla kwadratury Gaussa-Legendre'a\n")
    x_points_legendre = []
    y_points_legendre = []
    for n in range(2,21):
        legendre_roots,legendre_weights,legendre_sum = roots_legendre(n+2,True)

        legendre_result = calc_integral_legendre_method(0,2,n,legendre_roots,legendre_weights,f_for_legendre_method)

        x_points_legendre.append(n)
        y_points_legendre.append(abs( legendre_result - c_1_a(0,2)))
    plt.title(f'Błąd dla kwadratury Gaussa-Legendre\'a')
    plt.plot(x_points_legendre,y_points_legendre)
    plt.show()



    # print("\ndla kwadratury Gaussa-Laguerre'a\n")
    for k in (5,10):
        x_points_laguerre = []
        y_points_laguerre= []
        for n in range(2,21):
            laguerre_roots,laguerre_weights,laguerre_sum = roots_laguerre(n+2,True)

            laguerre_result = calc_integral_leguerre_method(n,laguerre_roots,laguerre_weights,f_for_laguerre_method,k)

            print(abs(laguerre_result - c_2_a(k)))
            x_points_laguerre.append(n)
            y_points_laguerre.append(abs(laguerre_result - c_2_a(k)))
        plt.title(f'Błąd dla kwadratury Gaussa-Laguerre\'a (k={k})')
        plt.plot(x_points_laguerre,y_points_laguerre)
        plt.show()



    # print("\ndla kwadratury Gaussa-Hermite'a")
    x_points_hermite = []
    y_points_hermite = []
    for n in range (2,16):
        hermite_roots, hermite_weights = roots_hermite(n+2)
        # hermite_roots_y, hermite_weights_y = roots_hermite(n+2)
        hermite_result = calc_integral_hermite_method(n,hermite_roots,hermite_weights,f_for_gauss_hemite_method_x_part,f_for_gauss_hemite_method_y_part)

        # print(abs(hermite_result - c_dok)) 
        x_points_hermite.append(n)
        y_points_hermite.append(abs(hermite_result - c_dok))
    plt.title(f'Błąd dla kwadratury Gaussa-Hermite\'a')
    plt.plot(x_points_hermite,y_points_hermite)
    plt.show()



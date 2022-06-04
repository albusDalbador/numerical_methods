from struct import calcsize
from unittest import result
import numpy as np
import matplotlib.pyplot as plt
from math import *


def calc_series_value(i,x,m,k):
    return (-1)**i*((k*x)**(2*i+m+2))/(k**(m+1) * factorial(2*i+1) * (2*i + m +2))


def calc_sum_of_series(iterations,a,b,m,k):
    sum = 0.0
    for i in range (iterations):
        sum += calc_series_value(i,b,m,k) - calc_series_value(i,a,m,k)
    return sum


def f(x,m,k):
    return x**m*sin(k*x)


def calculate_integral(num_of_intervals,a,b,m,k):
    step = (b-a)/num_of_intervals
    i = 0.0
    x = a
    S_f = 0.0
    h = step/2
    while x < pi:
        S_f += 1/3 * h*(f(x,m,k) + 4*f(x+h,m,k) + f(x+2*h,m,k))
        x += 2*h
    return S_f




if __name__ == "__main__":
    m = 0.0
    k = 1.0


    # p = 5
    # n = 2*p+1

    # h = (b-a)/2

    # print(calc_sum_of_series(20,a,b,m,k))
    a = 0.0
    b = pi

    results = open("results.txt","w")
    accurancy = open("accurancy","w")

    for i in ([(0,1),(1,1),(5,5)]):
        m = i[0]
        k = i[1]
        print(m,k)
        print(str(m),str(k))
        results.write('\nDla m= ' + str(m) + ' i k = ' + str(k) + '\n')
        accurancy.write('\nDla m= ' + str(m) + ' i k = ' + str(k) + '\n')

        calc_mistake = []
        for p in (5,10,25,50,100):
            n = 2*p + 1
            # print(str(calculate_integral(n,a,b,m,k)))
            numeric_integral = calculate_integral(n,a,b,m,k)

            results.write(str(numeric_integral) + '\n')
            accurancy.write(str(abs(numeric_integral - calc_sum_of_series(20,a,b,m,k))) + '\n')

            calc_mistake.append(abs(numeric_integral - calc_sum_of_series(20,a,b,m,k)))
        
        print(calc_mistake)
        plt.title('Dla k =' + str(k) + ' oraz m= ' +str(m))
        plt.plot([11,21,51,101,201],calc_mistake)
        plt.show()

        
    results.close()
    accurancy.close()



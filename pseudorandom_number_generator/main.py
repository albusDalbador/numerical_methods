from cmath import sqrt
from math import *
from optparse import Values
import matplotlib.pyplot as plt
from collections import Counter


def probability_density(x,sigma,mu):
    return 1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2))

def normalize_points(points,modul):
    return list(map(lambda x: x/(modul+1), points))

def calculate_vatiation(values):
    averave = sum(values)/len(values)
    return sum(list(map(lambda x: (x - averave)**2,values)))/len(values)

def calculate_autocorrelation(values,shift,variation,mu): #serival correlation
    sum = 0.0
    for i in range(0,len(values)-shift):
        sum += (values[i]-mu) * (values[i+shift]-mu)
    return sum/((len(values) - shift)*variation**2)

# def draw_histogram(elements):
#     plt.hist(elements)
#     plt.show()

def draw_coverage(x_points): 
    plt.scatter(x_points[:-1],x_points[1:],s=1)
    plt.show()


def uniform_distribution_algorithm():
    x_prev = 10
    for (a,c,m) in ((123,1,2**15),(69069,1,2**32)):
        x_array_random = []
        while len(x_array_random) < 10**4:
            x_prev = (a*x_prev + c) % m
            x_array_random.append(x_prev)
        x_array_normalized = normalize_points(x_array_random,m)

        interval_statistic = [0]*12
        for x in x_array_normalized:
            interval_statistic[floor(x*12)] += 1
        print(calculate_autocorrelation(x_array_normalized,1000,calculate_vatiation(x_array_normalized),0.5))

        plt.hist(x_array_normalized,rwidth=0.95,bins=20)
        plt.show()


def normal_distribution_algorithm():
    a = 69069
    c = 1
    m = 2**32
    mu = 0.2
    sigma = 0.5
    random_values = []
    # y_random = 10
    # x_random = 10
    random_seed = 10
    while len(random_values) < 10**4:
        x_random = random_seed = (a*random_seed + c) % m
        y_random = random_seed = (a*random_seed + c) % m
        x_random_scaled = (x_random/(m+1) - 0.5)*3*sigma + mu
        y_random_scaled = y_random/(m+1)/(sigma*sqrt(2*pi))
        if (y_random_scaled < probability_density(x_random_scaled,sigma,mu)):
            random_values.append(x_random_scaled)
    plt.hist(random_values,bins=20)
    plt.show()


def testing():
    pass




if __name__ == "__main__":
    
    # uniform_distribution_algorithm()

    normal_distribution_algorithm()

    testing()
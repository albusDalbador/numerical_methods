from cmath import sqrt
from math import *
import matplotlib.pyplot as plt
from collections import Counter


def probability_density(x,sigma,mu):
    return 1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2))

def normalize_points(points,modul):
    return list(map(lambda x: x/(modul+1), points))

def draw_histogram(elements):
    plt.hist(elements,bins='auto')
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
        # print(interval_statistic)
        draw_histogram(interval_statistic)


def normal_distribution_algorithm():
    pass


def testing():
    pass




if __name__ == "__main__":
    
    uniform_distribution_algorithm()

    normal_distribution_algorithm()

    testing()
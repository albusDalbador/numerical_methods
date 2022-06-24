from cmath import sqrt
from math import *
from statistics import variance
import matplotlib.pyplot as plt


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

def scatter_coverage(x_points): 
    plt.scatter(x_points[:-1],x_points[1:],s=1)
    plt.show()

def draw_histogram(values):
    plt.hist(values,rwidth=0.9,bins=30)
    plt.show()

def calculate_values_in_intervals(values,sigma,mu):
    intervals = [0]*12
    for x in values:
        x_scaled = (x-mu)/(6*sigma) + sigma
        intervals[floor(x_scaled*12)] += 1
    return intervals

def calcualte_testing_statistics(intervals,sigma,mu):
    n = sum(intervals)
    start = -3*sigma + mu
    step = 6*sigma/ 12
    x_square = 0.0
    out = open("testing_output.dat","a")
    out.write("\nstep values from test statistic calculation\n")
    for i in range (0,12):
        p_i = probability_density(start+(i+1)*step,sigma,mu) - probability_density(start+i*step,sigma,mu)
        x_square += pow(intervals[i]-n*p_i,2)/(n*p_i)
        out.write(f'p_i = {round(p_i,5)}, n*p_i = {round(n*p_i,5)}\n')
    out.close()
    return x_square




#2.1
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

        # draw_histogram(x_array_normalized)
        # scatter_coverage(x_array_normalized)


#2.2
def normal_distribution_algorithm() -> list:
    a = 69069
    c = 1
    m = 2**32
    mu = 0.2
    sigma = 0.5
    random_values = []
    random_seed = 10
    while len(random_values) < 10**4:
        x_random = random_seed = (a*random_seed + c) % m
        y_random = random_seed = (a*random_seed + c) % m
        x_random_scaled = (x_random/(m+1) - 0.5)*6*sigma + mu
        y_random_scaled = y_random/(m+1)/(sigma*sqrt(2*pi))
        if (y_random_scaled < probability_density(x_random_scaled,sigma,mu)):
            random_values.append(x_random_scaled)
    # draw_histogram(random_values)
    return random_values


#2.3
def testing(values,sigma,mu):
    average = sum(values)/len(values)
    variation = calculate_vatiation(values)
    open("testing_output.dat","w").close()
    with open("testing_output.dat","a") as out:
        out.write(f'\nvariation : {variation}\naverage value : {average}\n')

    interval_statistics = calculate_values_in_intervals(values,sigma,mu)
    with open("testing_output.dat","a") as out:
        out.write("\nnumber of values in 12 subranges:\n" + ", ".join(list(map(str,interval_statistics))) + "\n")

    testing_scatistics = calcualte_testing_statistics(interval_statistics,sigma,mu)
    print(testing_scatistics)




if __name__ == "__main__":
    
    uniform_distribution_algorithm()

    normal_dist_points = normal_distribution_algorithm()

    testing(normal_dist_points,0.5,0.2)
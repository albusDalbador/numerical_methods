from lib2to3.pgen2.token import RPAR
import re
from time import process_time_ns
from xml.sax.handler import property_interning_dict
import numpy as np 
import math
import matplotlib.pyplot as plt

def func(x,y):
    return 5/2 * (x**2 - y)**2 + (1 - x)**2


def dfDx(f,x,y,delta):
    return (f(x+delta,y) - f(x-delta,y))/(delta*2)


def dfDy(f,x,y,delta):
    return (f(x,y+delta) - f(x,y-delta))/(2*delta)


def findMinimum(f,r_pair,maxIter,epsilon,delta,h):
    iteration = 0
    file = open("fxy.dat","a")
    while iteration < maxIter:
        df_dx = r_pair[0] - h*dfDx(f,r_pair[0],r_pair[1],delta)
        df_dy = r_pair[1] - h*dfDy(f,r_pair[0],r_pair[1],delta)
        r_next = (df_dx,df_dy)
        # print(iteration) #wychodzi 37 dla epsilon = 0.01
        file.write(f'{r_pair[0]} {r_pair[1]} {f(r_pair[0],r_pair[1])}\n')
        if math.sqrt((r_next[0] - r_pair[0])**2 + (r_next[1] - r_pair[1])**2) < epsilon:
            file.close()
            return r_next
        r_pair = r_next
        iteration += 1
    file.close()
    return r_pair

#tragically complicated function :(
def generateStepPoints(f,r_pair,maxIter,epsilon,delta,h):
    step_points = [[],[],[]]
    iteration = 0
    while iteration < maxIter:
        df_dx = r_pair[0] - h*dfDx(f,r_pair[0],r_pair[1],delta)
        df_dy = r_pair[1] - h*dfDy(f,r_pair[0],r_pair[1],delta)
        r_next = (df_dx,df_dy)
        step_points[0].append( r_pair[0] )
        step_points[1].append( r_pair[1] )
        step_points[2].append( func(r_pair[0],r_pair[1]) )
        if math.sqrt((r_next[0] - r_pair[0])**2 + (r_next[1] - r_pair[1])**2) < epsilon:
            return step_points
        r_pair = r_next
        iteration += 1
    return step_points


def drawChart(func,points):
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    plt.contourf(func,levels=[1,2,3])
    plt.show()




if __name__ == "__main__":
    delta = 0.0001
    r_init = (-0.75,1.75)
    h = 0.1
    MAX_ITERATION = 1000
    epsilon = 0.01

    minimum = findMinimum(func,r_init,MAX_ITERATION,epsilon,delta,h)
    # print(minimum)

    points = generateStepPoints(func,r_init,MAX_ITERATION,epsilon,delta,h)
    print(points)

    # plt.contourf(points[0],points[1],points[2])

    # test = [[],[],[]]
    # test[0].append(1)
    # test[0].append(1)
    # test[0].append(1)
    # print(test)

    # x = np.linspace(0, 5, 50)
    # y = np.linspace(0, 5, 40)

    # X, Y = np.meshgrid(x, y)
    # print(X)
    # print(x)
    # Z = func(X, Y)

    # x_points,y_points = np.meshgrid(points[0],points[1])
    # z_points = func(x_points,y_points)

    # # plt.contour(X, Y, Z, colors='black')
    # plt.contour(x_points,y_points,z_points,20,colors='black')
    # plt.plot(x_points,y_points)
    # plt.show()


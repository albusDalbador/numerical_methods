from lib2to3.pgen2 import driver
from multiprocessing.dummy import current_process
from unittest import result
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 1/(1+x**2)



def generateXPoints(start,end,N):
    result = []
    for i in range (N+1):
        result.append(start + (end-start)/N*i)
    return result



#difference quotient
def generateDQArray(func,n,x_points) :
    matrix = np.zeros((n+1,n+1))
    for i in range (n+1):
        matrix[i][0] = func(x_points[i])

    for i in range (1,n+1):
        for j in range (i,n+1):
            matrix[j][i]= (matrix[j][i-1] - matrix[j-1][i-1]) / (x_points[j] - x_points[j-i])
    
    derivatives = []
    # print(matrix)

    for i in range (n+1):
        derivatives.append(matrix[i][i])

    return derivatives



def calcInterpolatedPolynomialPoints(left,right,N):
    x_points = generateXPoints(left,right,N)
    derives = generateDQArray(func,N,x_points)

    points_for_chart = [[]]
    points_for_chart.append([])

    currentX = left
    while currentX <= right:
        resultValue = 0
        for i in range (N+1):
            stepProduct = 1
            for j in range (0,i):
                stepProduct *= currentX - x_points[j]

            resultValue += stepProduct * derives[i]

        points_for_chart[0].append(currentX)
        points_for_chart[1].append(resultValue)
        currentX = round(currentX + 0.1, 4)

    return points_for_chart




def drawChart(func,left,right):
    x_points = []
    y_points = []
    currentX = left
    while currentX <= right:
        x_points.append(currentX)
        y_points.append(func(currentX))
        currentX += 0.1
    plt.plot(x_points,y_points)
    # plt.show()




if __name__ == "__main__":
    N = 20
    leftBorder = -5
    rightBorder = 5

    drawChart(func,leftBorder,rightBorder)

    polynomial_chart_data = calcInterpolatedPolynomialPoints(leftBorder,rightBorder,N)

    plt.plot(polynomial_chart_data[0],polynomial_chart_data[1])
    plt.title("Wykres wielomianu interpolacyjnego dla n = 20")
    plt.show()
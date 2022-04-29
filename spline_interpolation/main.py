import numpy as np
import matplotlib.pyplot as plt


def defineX(startPoint,endPoint,numOfPoints):
    xPoints = []
    for i in range (numOfPoints +1):
        xPoints.append(startPoint + (endPoint-startPoint)/numOfPoints*i)
    return xPoints



def defineY(xPoints,func):
    yPoints = []
    for x in xPoints:
        yPoints.append(func(x))
    return yPoints



def defineLambda(xPoints):
    lambdas = []
    for i in range (1,len(xPoints)):
        lambdas.append(xPoints[i] - xPoints[i-1])
    return lambdas



def defineMu(lamdas):
    mu = []
    for x in lambdas:
        mu.append(1-x)
    return mu



def func(x):
    return 1/(1+x**2)


def generateMatrix(n,lambdas,mu):
    matrix = np.zeros(shape=(n,n))
    for i in range (0,n):

        for j in range (0,n):
            if (i == j):
                if (i!=0 and i != n-1):
                    matrix[i][j] = 2
                else:
                    matrix[i][j] = 1
            elif (i == j-1 and i != 0):
                matrix[i][j] = lambdas[i]
            elif (i == j + 1):
                matrix[i][j] = mu[i]

    matrix[-1][-2] = 0
    return matrix



def defineFreeElemVector(xPoints,yPoints):
    d = [0]
    for i in range (1,len(xPoints)-2):
        d.append(6/(xPoints[i+1] - xPoints[i-1])*((yPoints[i+1] - yPoints[i])/(xPoints[i+1]-xPoints[i]) - (yPoints[i] - yPoints[i-1])/(xPoints[i] - xPoints[i-1])))
    d.append(0)
    return d



def calculateInterpolatedFunction(func,startPoint,endPoint,numOfPoints,mVector):
    xPoints = defineX(startPoint,endPoint,numOfPoints)
    yPoints = defineY(xPoints,func)
    step = startPoint
    values = []
    i = 1
    while step < endPoint:
        if (step > xPoints[i]):
            i += 1
            if (xPoints[i] == endPoint):
                break
        print(step)
        values.append(mVector[i-1]*((xPoints[i] - step)**3)/(6*(xPoints[i] - xPoints[i-1])) + mVector[i]*((step - xPoints[i-1])**3)/(6*(xPoints[i] - xPoints[i-1])) + ((yPoints[i] - yPoints[i-1])/(xPoints[i] - xPoints[i-1]) - (xPoints[i] - xPoints[i-1])/6*(mVector[i] - mVector[i-1]))*(step - xPoints[i-1]) + yPoints[i-1] - mVector[i-1]*(xPoints[i] - xPoints[i-1])**2/6)
        step += 0.1
    return values


def drawPolynomial(yPoints,startPoint,endPoint):
    step = startPoint
    xPoints = []
    while step <= endPoint:
        xPoints.append(step)
        step += 0.1
    plt.plot(xPoints,yPoints)
    plt.show()


def drawFunc(startPoint,endPoint,func):
    step = startPoint;
    xPoints = []
    yPoints = []
    while step <= endPoint:
        xPoints.append(step)
        yPoints.append(func(step))
        step += 0.1
    plt.ylim(-0.2,3)
    plt.plot(xPoints,yPoints)
    # plt.show()





if __name__ == "__main__":

    startPoint = -5
    endPoint = 5
    numOfPoints = 5

    xPoints = defineX(startPoint,endPoint,numOfPoints)
    yPoints = defineY(xPoints,func)
    lambdas = defineLambda(xPoints)
    mu = defineMu(lambdas)

    # print(xPoints)
    # print(yPoints)


    # print(mu)
    # print(lambdas)

    # print(defineY(defineX(startPoint,endPoint,numOfPoints),func))

    matrix = generateMatrix(numOfPoints,lambdas,mu)
    # print(matrix)

    freeVector = defineFreeElemVector(xPoints,yPoints)
    # print(freeVector)

    mVector = np.linalg.solve(matrix,freeVector)
    # print(mVector)

    polynomialValues = calculateInterpolatedFunction(func,startPoint,endPoint,numOfPoints,mVector)

    # print(polynomialValues)

    drawFunc(startPoint,endPoint,func)
    drawPolynomial(polynomialValues,startPoint,endPoint)







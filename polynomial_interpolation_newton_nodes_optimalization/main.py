
import matplotlib.pyplot as plt

def func(x):
    return 1/(1+x**2)



def generateXPoints(firstPoint,lastPoint,numOfPoints):
    points = []
    for i in range(numOfPoints +1):
        points.append(firstPoint + (lastPoint-firstPoint)/numOfPoints * i)
    return points



def calcDerivative(func,xPoints,i,j):
    # print(func(xPoints[i]))
    if j == 0:
        return func(xPoints[i])
    else:
        return (calcDerivative(func,xPoints,i,j-1) - calcDerivative(func,xPoints,i-1,j-1)) / (xPoints[i] - xPoints[i-j])



def calcPolynomialValueAtPoint(func,xPoints,currentPoint,power):
    resultValue = 0
    for i in range (power+1):
        stepProduct = 1
        for j in range (i-1):
            stepProduct *= (currentPoint-xPoints[j])
        resultValue += calcDerivative(func,xPoints,i,i) * stepProduct
    return resultValue



def calcPolynomialPoints(func,startPoint,endPoint,numOfPoints):
    resultArray = []
    currentPoint = startPoint
    xPoints = generateXPoints(startPoint+1,endPoint-1,numOfPoints)
    while currentPoint <= endPoint:
        resultArray.append(calcPolynomialValueAtPoint(func,xPoints,currentPoint,numOfPoints))
        currentPoint += 0.1
    return resultArray



def drawFuncPlot(func,startPoint,endPoint):
    point = startPoint
    xPoints = []
    yPoints = []
    while point <= endPoint:
        xPoints.append(point)
        yPoints.append(func(point))
        point += 0.1
    plt.ylim(-3,2)
    plt.plot(xPoints,yPoints)




if __name__ == "__main__":
    print("kurwa")

    startPoint = -5
    endPoint = 5
    numOfPoints = 5

    points = generateXPoints(startPoint,endPoint,numOfPoints)
    print(points)

    print(calcDerivative(func,points,1,1))
    # print(func(-5),func(-3))

    # for i in (-5,-3,-1,1,3,5):
    #     print(calcPolynomialValueAtPoint(func,generateXPoints(-5,5,5),i,5), "  ", func(i))
    #     # print(func(i))

    polynomialArr  = calcPolynomialPoints(func,startPoint-1,endPoint+1,numOfPoints)

    i = startPoint
    xPoints = []
    for item in polynomialArr:
        # print(round(i,2) ,"  " ,item)
        xPoints.append(i)
        i += 0.1

    drawFuncPlot(func,startPoint-1,endPoint+1)

    plt.plot(xPoints,polynomialArr)
    plt.show()
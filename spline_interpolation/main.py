import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 1/(1+x**2)


def generateLambdas(h_array):
    lambdas = []
    for i in range(len(h_array) - 1):
        lambdas.append(h_array[i+1]/(h_array[i] + h_array[i+1]))
    return lambdas


def generateH(x_array):
    h_array = []
    for i in range(len(x_array)-1):
        h_array.append(x_array[i+1] - x_array[i]) 
    return h_array


def generateMu(lambda_array):
    mu = []
    for item in lambda_array:
        mu.append(1 - item)
    return mu


def generateX(begin,end,num_of_points):
    x_points = []
    for i in range(num_of_points+1):
        x_points.append(begin + (end - begin)/num_of_points*i)
    return x_points


def calculateY(x_points,func):
    y_points = []
    for x in x_points:
        y_points.append(func(x))
    return y_points


# def generateM():
#     pass


def calculate_d_column(h,y):
    d_column = [0] #!!!!! alpha = beta = 0
    for i in range(1,len(h)-1):
        d_column.append(6/(h[i] + h[i+1]) * ((y[i+1] - y[i])/h[i+1] - (y[i] - y[i-1])/h[i]) )
    d_column.append(0)
    return d_column


def A_i(i,y,h,m):
    return (y[i] - y[i-1])/h[i] - h[i]/6 * (m[i] - m[i-1])


def B_i(y_prev,m_prev,h_i):
    return y_prev - m_prev * (h_i ** 2)/6


def generate_matrix_A(mu,_lambda,num_of_points):
    matrix = np.zeros((num_of_points,num_of_points))
    matrix[0][0] = matrix[-1][-1] = 1
    for i in range (1,num_of_points-1):
        matrix[i][i] = 2
        matrix[i][i-1] = mu[i-1]
        matrix[i][i+1] = _lambda[i-1]
    return matrix


def calculate_s_i(m,x_points,h,y):
    x = x_points[0]
    s_array=[]
    i = 1
    while x <= x_points[-1]:
        s_array.append(m[i-1] * ((x_points[i] - x)**3)/(6 * h[i]) + m[i]*(x-x[i-1])**3/(6*h[i]) + A_i(i,y,h,m) * (x - x_points[i-1]) + B_i(y[i-1],m[i-1],h[i]))
    return s_array



if __name__ == "__main__":

    x_min = -5
    x_max = 5
    num_of_points = 10

    x_points = generateX(x_min,x_max,num_of_points)
    y_points = calculateY(x_points,func)

    h_array = generateH(x_points)
    lambda_array = generateLambdas(h_array)
    mu_array = generateMu(lambda_array)

    d_column = calculate_d_column(h_array,y_points)
    matrix_A = generate_matrix_A(mu_array,lambda_array,num_of_points)

    # print(d_column)
    # print(matrix_A)

    m_column = np.linalg.solve(matrix_A,d_column)

    print(m_column)

    

    # print(generateMu(generateLambdas(generateH(generateX(x_min,x_max,num_of_points)))))
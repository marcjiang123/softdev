import numpy as np
from scipy import constants
import scipy.integrate as integrate
from scipy import linalg
import random

arr1 = np.array([1,2,3,4,5])
arr2d = np.array([[1,3,5],[2,5,1],[2,3,8]])
arr2 = np.array([[[1,2],[3,4],[5,6]],[[4,5],[6,7],[8,9]],[[1,3],[4,57],[10,33]]]) 
print(arr2d)
#arr3 = np.zeros(2)
#arr3 = np.ones(2)
#arr3 = np.arange(10)
arr4 = np.empty((9,3,2))
print(arr4)
arr5 = arr4.reshape(1,3,18)
print(arr5)
# print(arr4[1][2])
# arr4[1][2] = 3
# print(arr4[1][2])
# print(arr4)
# print(arr2)
list = [[[1,2],[3,4],[5,6]],[[4,5],[6,7],[8,9]],[[1,3],[4,57],[10,33]]]
listArr = np.array(list)
#print(listArr)
# print (arr1.min())

for i in range(arr2d.shape[0]):
    for p in range(arr2d.shape[1]):
        print(arr2d[i][p])
#.shape for shape, .size for total elements, .ndim for dimensions

x = np.array([1, 2, 3, 4, 5])
f = lambda x: x ** 2
squares = f(x)
print(squares)
print(squares[squares < 10])
less10 = squares < 10
print(less10)

test = np.array([5,4,3,2,1])
print(test)
data = squares + test
print(data)

print(data.mean())
# .min, .max(), .sum()

print(arr2d.transpose())

# SCIPY
print(5*constants.lb)
print(constants.speed_of_light)

g = lambda y: y**2 + 3*y
result = integrate.quad(g,0,2)
print(result)

print(arr2d)
arr2dInverse = linalg.inv(arr2d)
print(arr2dInverse)

print(arr2d.dot(arr2dInverse))

A = np.array([[3, 2], [9, -2]])
B = np.array([[5], [6]])
print(np.linalg.solve(A, B))
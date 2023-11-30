#This program solves a system of equations.
# As input, it takes a natural number i (i>1) and another i lines, each line contains i+1 real number separated by a space: aj1,aj2...aji, bi.
# Where j is the line number.
# At the output, the program prints x1, x2, ...xi in one line separated by spaces if the system has a solution. the line “The matrix of the system is singular” if the determinant of the matrix is 0.
import numpy as np

# Input the count of equations
n = int(input())

#Entering coefficients and the right side of the system
coefficients = []
for _ in range(n):
    equation = input().split()
    coefficients.append([float(x) for x in equation])

# Creating a Matrix and Vector
A = np.array(coefficients, dtype='float')[:, :-1]  #Matrix (left side of the system)
b = np.array(coefficients, dtype='float')[:, -1]  # Vector (right side of the system)

# Solving a system of equations
try:
    x = np.linalg.solve(A, b)
    print(' '.join(str(val) for val in x))
except np.linalg.LinAlgError:
    print("The matrix of the system is singular")
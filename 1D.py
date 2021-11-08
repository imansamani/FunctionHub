import numpy as np


def features(xi):
    f = [1., xi, xi**2, xi**3, xi**4]
    return np.array(f)


def features_xi(xi):
    dfdxi = [0., 1., 2.*xi, 3.*xi**2, 4.*xi**3]
    return np.array(dfdxi)


def int_features(xi1, xi2):
    def int_f(xi):
        return np.array([xi, (xi ** 2)/2., (xi ** 3)/3., (xi ** 4)/4., (xi ** 5)/5.])
    return np.array(int_f(xi2) - int_f(xi1))


# Iman's Basis Functions

A = np.zeros((5, 5))

# node 0
x = 0.
A[0] = features(x)
A[1] = features_xi(x)

# node 1
A[2] = int_features(0.0, 1.0)

# node 2
x = 1.
A[3] = features(x)
A[4] = features_xi(x)

# Solving for basis functions
Ainv = np.linalg.inv(A)
b = np.array([0 for i in range(5)])

b[0] = 1.0

coeff = np.dot(Ainv, b)

print(round(coeff[0], 2), round(coeff[1], 2))
print(round(coeff[2], 2))
print(round(coeff[3], 2), round(coeff[4], 2))


# Basis Functions

A = np.zeros((5, 5))

# node 0
x = 0.
A[0] = features(x)
A[1] = features_xi(x)

# node 1
x = 1./2.
A[2] = features(x)

# node 2
x = 1.
A[3] = features(x)
A[4] = features_xi(x)

# Solving for basis functions
Ainv = np.linalg.inv(A)
b = np.array([0 for j in range(5)])

b[0] = 1.0

coeff = np.dot(Ainv, b)

print(round(coeff[0], 2), round(coeff[1], 2))
print(round(coeff[2], 2))
print(round(coeff[3], 2), round(coeff[4], 2))

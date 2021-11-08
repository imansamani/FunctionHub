import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pylab as plt


def plot_basis_data(nodes, data_at_nodes, title):
    x = nodes[:, 0]
    y = nodes[:, 1]
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ts = ax.plot_trisurf(x, y, data_at_nodes, cmap="viridis", linewidth=2)
    cbar = fig.colorbar(ts, fraction=0.024, pad=0.02)
    cbar.ax.tick_params(labelsize=9)
    ax.set_title(title)
    ax.set_xlabel(r'X', fontsize=12)
    ax.set_ylabel(r'Y', fontsize=12)
    # ax.set_xlim()
    # ax.set_ylim()
    # ax.set_zlim()
    # ax.view_init(elev=30)
    plt.show()


def features(xi, eta):
    f = [1.,
         xi, eta,
         xi ** 2, eta ** 2, xi * eta,
         xi ** 3, eta ** 3, xi ** 2 * eta, xi * eta ** 2,
         xi ** 4, eta ** 4, xi ** 3 * eta, xi * eta ** 3, xi ** 2 * eta ** 2]
    return np.array(f)


def features_xi(xi, eta):
    dfdxi = [0.,
             1., 0.0,
             2. * xi, 0.0, eta,
             3. * xi ** 2, 0.0, 2. * xi * eta, eta ** 2,
             4. * xi ** 3, 0.0, 3. * xi ** 2 * eta, eta ** 3, 2. * xi * eta ** 2]
    return np.array(dfdxi)


def features_eta(xi, eta):
    dfdeta = [0.,
              0.0, 1.,
              0.0, 2. * eta, xi,
              0.0, 3. * eta ** 2, xi ** 2, 2. * xi * eta,
              0.0, 4. * eta ** 3, xi ** 3, 3. * xi * eta ** 2, 2. * xi ** 2 * eta]
    return np.array(dfdeta)


def features_b(xi, eta):
    f = [xi ** 3 * eta ** 2 + xi ** 2 * eta ** 3, xi ** 4 * eta + xi * eta ** 4,
         xi ** 3 * eta + xi * eta ** 3, xi ** 2 * eta ** 2,
         xi ** 2 * eta + xi * eta ** 2,
         xi * eta]
    return np.array(f)


def features_xi_b(xi, eta):
    dfdxi = [3. * xi ** 2 * eta ** 2 + 2. * xi * eta ** 3, 4. * xi ** 3 * eta + eta ** 4,
             3. * xi ** 2 * eta + eta ** 3, 2. * xi * eta ** 2,
             2. * xi * eta + eta ** 2,
             eta]
    return np.array(dfdxi)


def features_eta_b(xi, eta):
    dfdeta = [2. * xi ** 3 * eta + 3. * xi ** 2 * eta ** 2, xi ** 4 + 4. * xi * eta ** 3,
              xi ** 3 + 3. * xi * eta ** 2, 2. * xi ** 2 * eta,
              xi ** 2 + 2. * xi * eta,
              xi]
    return np.array(dfdeta)


# Basis Functions

A = np.zeros((15, 15))

# node 0
x = 0.
y = 0.
A[0] = features(x, y)
A[1] = features_xi(x, y)
A[2] = features_eta(x, y)

# node 1
x = 1./2.
y = 0.
A[3] = features(x, y)
A[4] = -features_eta(x, y)

# node 2
x = 1.
y = 0.
A[5] = features(x, y)
A[6] = features_xi(x, y)
A[7] = features_eta(x, y)

# node 3
x = 1./2.
y = 1./2.
A[8] = features(x, y)
A[9] = features_xi(x, y) + features_eta(x, y)

# node 4
x = 0.
y = 1.
A[10] = features(x, y)
A[11] = features_xi(x, y)
A[12] = features_eta(x, y)

# node 5
x = 0.
y = 1./2.
A[13] = features(x, y)
A[14] = -features_xi(x, y)

# Solving for basis functions
Ainv = np.linalg.inv(A)
b = np.array([0 for i in range(15)])

b[0] = 1.0

coeff = np.dot(Ainv, b)

print(round(coeff[0], 2), round(coeff[1], 2), round(coeff[2], 2))
print(round(coeff[3], 2), round(coeff[4], 2))
print(round(coeff[5], 2), round(coeff[6], 2), round(coeff[7], 2))
print(round(coeff[8], 2), round(coeff[9], 2), )
print(round(coeff[10], 2), round(coeff[11], 2), round(coeff[12], 2))
print(round(coeff[13], 2), round(coeff[14], 2))


N = 50
xi = np.linspace(0., 1., N)
eta = np.linspace(0., 1., N)
nodes = []
for i in range(N):
    for j in range(N):
        if eta[j] <= 1. - xi[i]:
            nodes.append([xi[i], eta[j]])
nodes = np.array(nodes)

# phi -->
data = []
for node in nodes:
    xi = node[0]
    eta = node[1]
    data.append(np.sum(coeff*features(xi, eta)))
plot_basis_data(nodes, data, r"$\Phi$")


# Buble Function

A = np.zeros((6, 6))

x = 1./2.
y = 0.0
A[0] = -features_eta_b(x, y)


x = 1.0
y = 0.0
A[1] = features_eta_b(x, y)

x = 1./2.
y = 1./2.
A[2] = features_b(x, y)
A[3] = features_xi_b(x, y) + features_eta_b(x, y)

A[4] = features_b(1./4., 1./4.) - features_b(1./2., 1./4.)

A[5] = features_b(1./4., 1./4.)

if np.abs(np.linalg.det(A)) < 1.0e-12:
    print("Warning: Det is 0:" + str(np.linalg.det(A)))
    exit()

Ainv = np.linalg.inv(A)
b = np.array([0 for i in range(6)])
b[5] = 1.

coeff = np.dot(Ainv, b)
coeff = coeff/np.min(abs(coeff))

print(coeff)

N = 50
xi = np.linspace(0., 1., N)
eta = np.linspace(0., 1., N)
nodes = []
for i in range(N):
    for j in range(N):
        if eta[j] <= 1. - xi[i]:
            nodes.append([xi[i], eta[j]])
nodes = np.array(nodes)

# bubble -->
data = []
for node in nodes:
    xi = node[0]
    eta = node[1]
    data.append(np.sum(coeff*features_b(xi, eta)))
plot_basis_data(nodes, data, r"Bubble")

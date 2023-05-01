"""
Author: Iman Samani
Date: 05/01/2023
Description: Determines if a point p is inside a triangle defined by vertices v1, v2, v3.
Returns True if the point is inside the triangle, False otherwise.
"""

import numpy as np


def area(triangle):
    e1 = triangle[1] - triangle[0]
    e2 = triangle[2] - triangle[0]
    return 0.5 * np.linalg.norm(np.cross(e1, e2))


def point_in_triangle(point, triangle):
    a = 0
    for i in range(3):
        a += area([point, triangle[i-1], triangle[i]])
    if a == area(triangle):
        return True
    else:
        return False


if __name__ == "__main__":
    v0 = np.array([1., 0., 0.])
    v1 = np.array([0., 1., 0.])
    v2 = np.array([0., 0., 1.])

    tri = [v0,v1,v2]

    p = np.array([0.25, 0.25, 0.5])
    print("Here we expect a True: ", point_in_triangle(p, tri))

    p = np.array([0.5, 0.5, 0.5])
    print("Here we expect a Fales: ", point_in_triangle(p, tri))

/*
Author: Iman Samani
Date: 05/01/2023
Description: Determines if a point p is inside a triangle defined by vertices v1, v2, v3.
Returns True if the point is inside the triangle, False otherwise.
*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double area(vector<vector<double>> triangle) {
    vector<double> e1 = {triangle[1][0] - triangle[0][0], triangle[1][1] - triangle[0][1], triangle[1][2] - triangle[0][2]};
    vector<double> e2 = {triangle[2][0] - triangle[0][0], triangle[2][1] - triangle[0][1], triangle[2][2] - triangle[0][2]};
    vector<double> cross = {e1[1]*e2[2] - e1[2]*e2[1], e1[2]*e2[0] - e1[0]*e2[2], e1[0]*e2[1] - e1[1]*e2[0]};
    return 0.5 * sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);
}

bool point_in_triangle(vector<double> point, vector<vector<double>> triangle) {
    double a = 0;
    for (int i = 0; i < 3; i++) {
        vector<vector<double>> subtri = {point, triangle[i], triangle[(i+1)%3]};
        a += area(subtri);
    }
    if (a == area(triangle)) {
        return true;
    } else {
        return false;
    }
}

int main() {
    vector<double> v0 = {1., 0., 0.};
    vector<double> v1 = {0., 1., 0.};
    vector<double> v2 = {0., 0., 1.};

    vector<vector<double>> tri = {v0, v1, v2};

    vector<double> p = {0.25, 0.25, 0.5};
    cout << "Here we expect a True: " << point_in_triangle(p, tri) << endl;

    p = {0.5, 0.5, 0.5};
    cout << "Here we expect a False: " << point_in_triangle(p, tri) << endl;

    return 0;
}

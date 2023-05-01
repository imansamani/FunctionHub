import numpy as np


l4t1 = -1.0
l4w1 = 1.0 / 6.0
l4t2 = -np.sqrt(1.0 / 5.0)
l4w2 = 5.0 / 6.0
l4t3 = np.sqrt(1.0 / 5.0)
l4w3 = 5.0 / 6.0
l4t4 = 1.0
l4w4 = 1.0 / 6.0


def int5(t1, t2, x1, x2, f, dfdx):

    def time_conversion(t):
        return t2mt1O2 * t + t2pt1O2

    def space_integral(fl, fpl, fm, fr, fpr):
        return x2mx1O60 * (14. * (fl + fr) + x2mx1 * (fpl - fpr) + 32. * fm)

    xl = x1
    xr = x2
    xm = (x2 + x1) / 2.0

    x2mx1 = x2 - x1
    x2mx1O60 = x2mx1 / 60.

    t2mt1O2 = (t2 - t1) / 2.
    t2pt1O2 = (t2 + t1) / 2.

    fl = f(time_conversion(l4t1), xl)
    fpl = dfdx(time_conversion(l4t1), xl)
    fm = f(time_conversion(l4t1), xm)
    fr = f(time_conversion(l4t1), xr)
    fpr = dfdx(time_conversion(l4t1), xr)
    f1 = space_integral(fl, fpl, fm, fr, fpr)

    fl = f(time_conversion(l4t2), xl)
    fpl = dfdx(time_conversion(l4t2), xl)
    fm = f(time_conversion(l4t2), xm)
    fr = f(time_conversion(l4t2), xr)
    fpr = dfdx(time_conversion(l4t2), xr)
    f2 = space_integral(fl, fpl, fm, fr, fpr)

    fl = f(time_conversion(l4t3), xl)
    fpl = dfdx(time_conversion(l4t3), xl)
    fm = f(time_conversion(l4t3), xm)
    fr = f(time_conversion(l4t3), xr)
    fpr = dfdx(time_conversion(l4t3), xr)
    f3 = space_integral(fl, fpl, fm, fr, fpr)

    fl = f(time_conversion(l4t4), xl)
    fpl = dfdx(time_conversion(l4t4), xl)
    fm = f(time_conversion(l4t4), xm)
    fr = f(time_conversion(l4t4), xr)
    fpr = dfdx(time_conversion(l4t4), xr)
    f4 = space_integral(fl, fpl, fm, fr, fpr)

    return t2mt1O2 * (l4w1 * f1 + l4w2 * f2 + l4w3 * f3 + l4w4 * f4)


def integrand(t, x):
    return np.sin(t+x)


def dintegranddx(t, x):
    return np.cos(t+x)


print(integrate(1., 2., 3., 4., integrand, dintegranddx))

#!/usr/bin/python

from numpy import *

def compute_error(b, w, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points))

def run():
    points = genfromtxt("data.csv", delimiter=",")

    x_total = 0.0
    y_total = 0.0
    for i in range(0, len(points)):
        x_total = x_total + points[i, 0]
        y_total = y_total + points[i, 1]
    x_avg = x_total / float(len(points))
    y_avg = y_total / float(len(points))

    v1 = 0.0
    v2 = 0.0
    for i in range(0, len(points)):
        v1 = v1 + (points[i, 0] - x_avg) * (points[i, 1] - y_avg)
        v2 = v2 + (points[i, 0] - x_avg) ** 2

    w = v1 / v2
    b = y_avg - x_avg * w

    print "Starting gradient descent at b = {0}, w = {1}, error = {2}".format(b, w, compute_error(b, w, points))

if __name__ == '__main__':
    run()

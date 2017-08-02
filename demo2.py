#!/usr/bin/python

from numpy import *

# y = mx + b
# m is slope, b is y-intercept

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
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

    initial_m = v1 / v2
    initial_b = y_avg - x_avg * initial_m

    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))

if __name__ == '__main__':
    run()

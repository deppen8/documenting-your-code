import numpy as np
from scipy.stats import poisson, uniform


def generate_poisson_points(bounds, rate):
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    N = poisson(rate * dx * dy).rvs()
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0]
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]

    return np.hstack((xs, ys))

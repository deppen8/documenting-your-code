import numpy as np
from scipy.stats import poisson, uniform
# from typing import Tuple # Tuple has been deprecated in pyton 3.9

def generate_poisson_points(
        bounds: tuple[float,float,float,float], 
        rate: float
    ) -> np.ndarray:
    """Generates a numpy array of 2D points within 2D bounds

    Args:
        bounds: (xmin, ymin, xmax, ymax)
        rate: per-unit fill

    Returns:
        np.ndarray: 2D numpy array
    """
    # extract xy ranges from the bounds
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    # generate random values
    N = poisson(rate * dx * dy).rvs() 
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0] 
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]
    
    # packing the output into a numpy array
    return np.hstack((xs, ys))

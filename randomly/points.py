from typing import Tuple

import numpy as np
from scipy.stats import poisson, uniform


def generate_poisson_points(
    bounds: Tuple[float, float, float, float], rate: float
) -> np.ndarray:
    """Create coordinate pairs from a Poisson process

    Parameters
    ----------
    bounds : Tuple[float, float, float, float]
        ``(minx, miny, maxx, maxy)`` of the bounding box
    rate : float
        Theoretical events per unit area across the whole space. See Notes for more details.

    Returns
    -------
    np.ndarray
        Array of shape ``(N pairs, 2)`` where each pair is x and y coordinates inside the bounding box.
    """

    # Get sizes of sides of the area of interest
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    # Draw random values from Poisson distribution
    # to determine how many points to place
    N = poisson(rate * dx * dy).rvs()

    # Draw N random x and y coordinate values
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0]
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]

    return np.hstack((xs, ys))

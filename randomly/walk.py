# https://matplotlib.org/stable/gallery/animation/random_walk.html#sphx-glr-gallery-animation-random-walk-py

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)


def _random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


def _update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines


def plot_random_walk(num_steps, num_walks):
    walks = [_random_walk(num_steps) for index in range(num_walks)]

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    lines = [ax.plot([], [], [])[0] for _ in walks]

    ax.set(xlim3d=(0, 1), xlabel="X")
    ax.set(ylim3d=(0, 1), ylabel="Y")
    ax.set(zlim3d=(0, 1), zlabel="Z")

    _ = animation.FuncAnimation(
        fig, _update_lines, num_steps, fargs=(walks, lines), interval=100
    )

    plt.show()


plot_random_walk(30, 40)

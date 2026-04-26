import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

import numpy as np


def draw_robot(mu, color, W):
    x, y, theta = mu[0, 0], mu[1, 0], mu[2, 0]

    e = Ellipse([x, y], W, W, angle=theta, edgecolor=color, fill=False)
    plt.gca().add_artist(e)

    r_mat = np.array([[np.cos(theta), -1 * np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]]) 
    dir_vec = np.dot(r_mat, np.array([W, 0]))
    plt.plot(x + np.array([0, dir_vec[0]]), y + np.array([0, dir_vec[1]]), color=color, linewidth=1)

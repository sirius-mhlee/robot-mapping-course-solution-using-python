import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

import numpy as np

def drawrobot(xvec, color, W, L):
    x, y, theta = xvec[0, 0], xvec[1, 0], xvec[2, 0]

    e = Ellipse([x, y], W + 0.015, W + 0.015, angle=theta, edgecolor=color, fill=False)
    plt.gca().add_artist(e)

    rmat = np.array([[np.cos(theta), -1 * np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]]) 
    dirvec = np.dot(rmat, np.array([W + 0.015, 0]))
    plt.plot(x + np.array([0, dirvec[0]]), y + np.array([0, dirvec[1]]), color=color, linewidth=1)

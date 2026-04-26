import sys
import matplotlib.pyplot as plt

import numpy as np

sys.path.append('../tool')
from draw_robot import *


def plot_state(mu, landmarks, timestep, z):
    plt.title('Tutorial timestep {}'.format(timestep))

    plt.plot(landmarks['x'], landmarks['y'], 'kP', markersize=10, linewidth=5)

    for i in range(len(z)):
        mX = landmarks['x'][z[i]['id']]
        mY = landmarks['y'][z[i]['id']]
        plt.plot([mu[0, 0], mX], [mu[1, 0], mY], color='b', linewidth=1)

    draw_robot(mu, 'r', 0.3)

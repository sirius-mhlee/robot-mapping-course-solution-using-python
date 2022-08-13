import sys
import matplotlib.pyplot as plt

import numpy as np

sys.path.append('../tool')
from drawrobot import *

def plot_state(mu, landmarks, timestep, z):
    plt.plot(landmarks['x'], landmarks['y'], 'kP', markersize=10, linewidth=5)

    for i in range(len(z)):
        mX = landmarks['x'][z[i]['id']]
        mY = landmarks['y'][z[i]['id']]
        plt.plot([mu[0, 0], mX], [mu[1, 0], mY], color='b', linewidth=1)

    drawrobot(mu, 'r', 0.3, 0.3)

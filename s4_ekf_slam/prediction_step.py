import sys

import numpy as np

sys.path.append('../tool')
from normalize_angle import *


def prediction_step(mu, sigma, u):
    theta = mu[2, 0]
    heading = theta + u['r1']

    mu[0, 0] = mu[0, 0] + u['t'] * np.cos(heading)
    mu[1, 0] = mu[1, 0] + u['t'] * np.sin(heading)
    mu[2, 0] = normalize_angle(mu[2, 0] + u['r1'] + u['r2'])

    dim = sigma.shape[0]

    G = np.eye(dim)
    G[0, 2] = -u['t'] * np.sin(heading)
    G[1, 2] = u['t'] * np.cos(heading)

    motion_noise = 0.1
    R = np.zeros_like(sigma)
    R[0:3, 0:3] = np.diag([motion_noise, motion_noise, motion_noise / 10])

    sigma = G @ sigma @ G.T + R
    return mu, sigma

import sys
import numpy as np

sys.path.append('../tool')
from normalize_angle import *


def motion_command(mu, u):
    mu[0, 0] = mu[0, 0] + u['t'] * np.cos(normalize_angle(mu[2, 0] + u['r1']))
    mu[1, 0] = mu[1, 0] + u['t'] * np.sin(normalize_angle(mu[2, 0] + u['r1']))
    mu[2, 0] = normalize_angle(mu[2, 0] + u['r1'] + u['r2'])
    return mu

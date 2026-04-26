import sys

import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera

from correction_step import *
from plot_state import *
from prediction_step import *

sys.path.append('../tool')
from read_sensor import *
from read_world import *


INF = 1000


landmarks = read_world('../data/world.dat')
data = read_sensor('../data/sensor.dat')

landmark_count = len(landmarks['id'])
dim = 2 * landmark_count + 3

observed_landmarks = np.zeros(landmark_count, dtype=bool)

mu = np.zeros((dim, 1))
sigma = np.zeros((dim, dim))
sigma[3:, 3:] = INF * np.eye(2 * landmark_count)

fig = plt.figure(figsize=(8, 8))
plt.cla()
plt.grid(True)
plt.xlim([-2, 12])
plt.ylim([-2, 12])

camera = Camera(fig)

for t in range(len(data['sensor'])):
    mu, sigma = prediction_step(mu, sigma, data['odometry'][t])
    mu, sigma, observed_landmarks = correction_step(
        mu,
        sigma,
        data['sensor'][t],
        observed_landmarks,
    )

    plot_state(mu, sigma, landmarks, t + 1, observed_landmarks, data['sensor'][t])
    camera.snap()

camera.animate(interval=50, blit=True).save('result.gif')

print('Final robot pose:')
print(mu[0:3])
print('Final robot covariance:')
print(sigma[0:3, 0:3])

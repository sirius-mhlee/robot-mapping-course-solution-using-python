import sys
import matplotlib.pyplot as plt
import numpy as np

from celluloid import Camera

from motion_command import *
from plot_state import *

sys.path.append('../tool')
from read_world import *
from read_sensor import *


landmarks = read_world('../data/world.dat')
data = read_sensor('../data/sensor.dat')

mu = np.zeros((3, 1))

fig = plt.figure(figsize=(8, 8))
plt.cla()
plt.grid(True)
plt.xlim([-2, 12])
plt.ylim([-2, 12])

camera = Camera(fig)

for t in range(len(data['sensor'])):

    mu = motion_command(mu, data['odometry'][t])

    plot_state(mu, landmarks, t + 1, data['sensor'][t])
    camera.snap()

camera.animate(interval=50, blit=True).save('result.gif')

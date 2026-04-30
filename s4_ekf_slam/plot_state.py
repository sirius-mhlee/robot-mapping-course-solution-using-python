import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

sys.path.append('../tool')
from draw_robot import *

from correction_step import landmark_state_index


def draw_probability_ellipse(mean, covariance, color):
    covariance = covariance[0:2, 0:2]
    values, vectors = np.linalg.eigh(covariance)
    values = np.maximum(values, 0)

    order = values.argsort()[::-1]
    values = values[order]
    vectors = vectors[:, order]

    angle = np.degrees(np.arctan2(vectors[1, 0], vectors[0, 0]))
    scale = np.sqrt(-2 * np.log(1 - 0.6))
    width, height = 2 * scale * np.sqrt(values)

    ellipse = Ellipse(
        xy=(mean[0, 0], mean[1, 0]),
        width=width,
        height=height,
        angle=angle,
        edgecolor=color,
        facecolor='none',
        linewidth=1,
    )
    plt.gca().add_patch(ellipse)


def plot_state(mu, sigma, landmarks, timestep, observed_landmarks, z):
    plt.plot(landmarks['x'], landmarks['y'], 'k+', markersize=10, linewidth=5)

    draw_probability_ellipse(mu[0:3], sigma[0:3, 0:3], 'r')

    for landmark_id, observed in enumerate(observed_landmarks):
        if observed:
            landmark_index = landmark_state_index(landmark_id)
            plt.plot(mu[landmark_index, 0], mu[landmark_index + 1, 0], 'bo', markersize=6)
            draw_probability_ellipse(
                mu[landmark_index:landmark_index + 2],
                sigma[landmark_index:landmark_index + 2, landmark_index:landmark_index + 2],
                'b',
            )

    for measurement in z:
        landmark_index = landmark_state_index(measurement['id'])
        plt.plot(
            [mu[0, 0], mu[landmark_index, 0]],
            [mu[1, 0], mu[landmark_index + 1, 0]],
            color='k',
            linewidth=1,
        )

    draw_robot(mu[0:3], 'r', 0.3)

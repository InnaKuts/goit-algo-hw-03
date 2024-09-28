import sys

import matplotlib.pyplot as plt
import numpy as np


def koch_curve(p1, p2, order):
    if order == 0:
        return [p1, p2]
    else:
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = (p2 - p1) / 3
        p3 = p1 + delta
        p5 = p1 + 2 * delta
        angle = -np.pi / 3
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        p4 = p3 + np.dot(rotation_matrix, delta)

        return (
            koch_curve(p1, p3, order - 1) +
            koch_curve(p3, p4, order - 1) +
            koch_curve(p4, p5, order - 1) +
            koch_curve(p5, p2, order - 1)
        )


def koch_snowflake(order, scale=10):
    p1 = np.array([0, 0])
    p2 = np.array([scale, 0])
    angle = 2 * np.pi / 3
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    p3 = p2 + np.dot(rotation_matrix, p2 - p1)

    points = np.array(
        koch_curve(p1, p2, order) +
        koch_curve(p2, p3, order)[1:] +
        koch_curve(p3, p1, order)[1:]
    )

    return points


def draw_koch_snowflake(order):
    points = koch_snowflake(order)
    plt.plot(points[:, 0], points[:, 1], color='b')
    plt.axis('equal')
    plt.title(f'Koch Snowflake: {order}')
    plt.show()


def safe(func, default):
    try:
        return func()
    except:
        return default


def main():
    order = safe(lambda: int(sys.argv[1]), None)
    if order is None:
        order = safe(lambda: int(input('Enter recursion level (default = 5): ')), 5)
    draw_koch_snowflake(order)


if __name__ == '__main__':
    main()

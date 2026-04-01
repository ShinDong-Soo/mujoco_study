import math
import time
import sys
from pathlib import Path

import numpy as np
import mujoco
import mujoco.viewer


def solve_ik_2d(x, y, l1, l2):
    r2 = x * x + y * y
    cos_theta2 = (r2 - l1 * l1 - l2 * l2) / (2 * l1 * l2)
    cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)

    theta2 = math.acos(cos_theta2)

    k1 = l1 + l2 * math.cos(theta2)
    k2 = l2 * math.sin(theta2)
    theta1 = math.atan2(y, x) - math.atan2(k2, k1)

    return theta1, theta2


def make_circle_points(center=(0.55, 0.2), radius=0.15, num_points=200):
    cx, cy = center
    points = []

    for t in np.linspace(0, 2 * np.pi, num_points, endpoint=False):
        x = cx + radius * np.cos(t)
        y = cy + radius * np.sin(t)
        points.append((x, y))

    return points


def make_square_points(center=(0.55, 0.2), size=0.25, points_per_edge=50):
    cx, cy = center
    h = size / 2

    p1 = (cx - h, cy - h)
    p2 = (cx + h, cy - h)
    p3 = (cx + h, cy + h)
    p4 = (cx - h, cy + h)

    points = []

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p1[0] + (p2[0] - p1[0]) * t,
            p1[1] + (p2[1] - p1[1]) * t
        ))

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p2[0] + (p3[0] - p2[0]) * t,
            p2[1] + (p3[1] - p2[1]) * t
        ))

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p3[0] + (p4[0] - p3[0]) * t,
            p3[1] + (p4[1] - p3[1]) * t
        ))

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p4[0] + (p1[0] - p4[0]) * t,
            p4[1] + (p1[1] - p4[1]) * t
        ))

    return points


def make_triangle_points(center=(0.55, 0.2), size=0.25, points_per_edge=70):
    cx, cy = center
    h = size

    p1 = (cx, cy + h / 2)
    p2 = (cx - h / 2, cy - h / 2)
    p3 = (cx + h / 2, cy - h / 2)

    points = []

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p1[0] + (p2[0] - p1[0]) * t,
            p1[1] + (p2[1] - p1[1]) * t
        ))

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p2[0] + (p3[0] - p2[0]) * t,
            p2[1] + (p3[1] - p2[1]) * t
        ))

    for t in np.linspace(0, 1, points_per_edge, endpoint=False):
        points.append((
            p3[0] + (p1[0] - p3[0]) * t,
            p3[1] + (p1[1] - p3[1]) * t
        ))

    return points


def make_path(shape):
    if shape == "circle":
        return make_circle_points()
    if shape == "square":
        return make_square_points()
    if shape == "triangle":
        return make_triangle_points()

    raise ValueError("shape must be 'circle', 'square', or 'triangle'")


def get_shape_from_args():
    if len(sys.argv) > 1:
        shape = sys.argv[1].lower()
    else:
        shape = "circle"

    valid_shapes = {"circle", "square", "triangle"}
    if shape not in valid_shapes:
        raise ValueError(
            f"Invalid shape: {shape}. Use one of: circle, square, triangle"
        )

    return shape


def main():
    shape = get_shape_from_args()
    print(f"Selected shape: {shape}")

    xml_path = Path(__file__).parent / "arm26.xml"
    model = mujoco.MjModel.from_xml_path(str(xml_path))
    data = mujoco.MjData(model)

    l1 = 0.5
    l2 = 0.5
    path_points = make_path(shape)

    # 초기 자세 세팅
    first_x, first_y = path_points[0]
    theta1, theta2 = solve_ik_2d(first_x, first_y, l1, l2)
    data.qpos[0] = theta1
    data.qpos[1] = theta2
    mujoco.mj_forward(model, data)

    with mujoco.viewer.launch_passive(model, data) as viewer:
        idx = 0

        while viewer.is_running():
            x, y = path_points[idx]
            theta1, theta2 = solve_ik_2d(x, y, l1, l2)

            data.qpos[0] = theta1
            data.qpos[1] = theta2

            mujoco.mj_forward(model, data)
            viewer.sync()

            idx = (idx + 1) % len(path_points)
            time.sleep(0.03)


if __name__ == "__main__":
    main()

# python ik_draw_shapes_with_arm.py circle
# python ik_draw_shapes_with_arm.py square
# python ik_draw_shapes_with_arm.py triangle
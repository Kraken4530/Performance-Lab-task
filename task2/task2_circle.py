import sys


def point_inside_circle(x: float, y: float, r: float, point: tuple) -> int:
    px, py = point
    s = (px - x) ** 2 + (py - y) ** 2
    if s < r ** 2:
        return 1
    elif s == r ** 2:
        return 0
    else:
        return 2


def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    with open(circle_file, 'r') as f:
        xy = f.readline().strip().split()
        x = float(xy[0])
        y = float(xy[1])
        r = float(f.readline().strip())
    with open(points_file, 'r') as f:
        xy_points = f.readlines()
    points = []
    for line in xy_points:
        if line.strip():
            point_xy = line.strip().split()
            point = (float(point_xy[0]), float(point_xy[1]))
            points.append(point)
    for point in points:
        result = point_inside_circle(x, y, r, point)
        print(result)


if __name__ == "__main__":
    main()

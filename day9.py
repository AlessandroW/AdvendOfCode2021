import numpy as np


TEST = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def parse(input):
    return np.array([[int(char) for char in row]
                     for row in input.split("\n")
                     if len(row) > 0])

def get_neighborhood(i, j, max_i, max_j):
    result = []
    if i > 0:
        result.append((i-1, j))
    if j > 0:
        result.append((i, j-1))
    if i < max_i:
        result.append((i+1, j))
    if j < max_j:
        result.append((i, j+1))
    return result

def is_lowest(i, j, array, max_i, max_j):
    return all(array[i, j] < array[a, b] for a, b in get_neighborhood(i, j, max_i, max_j))

assert get_neighborhood(0, 0, 1, 1) == [(1, 0), (0, 1)], get_neighborhood(0, 0, 1, 1)
assert get_neighborhood(1, 1, 2, 2) == [(0, 1), (1, 0), (2, 1), (1, 2)], get_neighborhood(1, 1, 2, 2)

def part1(input):
    array = parse(input)
    max_i = len(array) - 1
    max_j = len(array[0]) - 1
    lowest_points = np.array([[is_lowest(i, j, array, max_i, max_j)
                            for j in range(max_j + 1)]
                            for i in range(max_i + 1)])
    low_points = array[lowest_points]
    print(sum(low_points + 1))

with open('day9.txt') as f:
    input = f.read()

part1(input)

def part2(input):
    array = parse(input)
    max_i = len(array) - 1
    max_j = len(array[0]) - 1
    lowest_points = np.array([[is_lowest(i, j, array, max_i, max_j)
                            for j in range(max_j + 1)]
                            for i in range(max_i + 1)])
    low_points = array[lowest_points]

    def distance(from_i, from_j, to_i, to_j, array):
        result = min(int(np.any(array[min(from_i, to_i):max(from_i, to_i)+1, from_j] == 9))
                    + int(np.any(array[to_i, min(from_j, to_j):max(from_j, to_j)] == 9)),
                    int(np.any(array[min(from_i, to_i):max(from_i, to_i)+1, to_j] == 9))
                    + int(np.any(array[from_i, min(from_j, to_j):max(from_j, to_j)] == 9)))
        return result


    low_points_coords = np.argwhere(lowest_points)
    clusters = [[] for i in range(len(low_points_coords))]

    for from_i, from_j in np.argwhere(array != 9):
        result = [distance(from_i, from_j, i, j, array)
                            for i, j in low_points_coords]
        if np.min(result) != 0:
            import pdb; pdb.set_trace()
        result = np.argmin(result)
        clusters[result].append(array[from_i, from_j])

    clusters = sorted(clusters)
    print(len(clusters[-1]) * len(clusters[-2]) * len(clusters[-3]))

part2(input)

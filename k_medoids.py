import math
import matplotlib.pyplot as plt

def k_medoids(data, k):
    pass

def distance_matrix(data):
    matrix = []
    for entry in data:
        entry_coords = entry[1:-1]
        entry_dists = []
        for other_entry in data:
            other_entry_coords = other_entry[1:-1]
            distance_between = _distance(entry_coords, other_entry_coords)
            entry_dists.append(round(distance_between, 3))
        matrix.append(entry_dists)
    return matrix

def _distance(point1, point2):
    dist = 0
    for i in range(len(point1)):
        dist += ( point1[i] - point2[i] ) ** 2
        return math.sqrt(dist)

def plot(data):
    xs = [line[1] for line in data]
    ys = [line[2] for line in data]
    plt.plot(xs, ys, '+')
    plt.show()

if __name__ == '__main__':
    data = [
        ['Gene1',  1.1,  1.9, 'C1'],
        ['Gene2',  2.5,  3.8, 'C2'],
        ['Gene3',  2.45, 2.4, 'C3'],
        ['Gene4',  1.8,  4.8, 'C2'],
        ['Gene5',  2.3,  3.7, 'C2'],
        ['Gene6',  4.8,  0.8, 'C3'],
        ['Gene7',  1.9,  1.1, 'C1'],
        ['Gene8',  1.2,  0.6, 'C1'],
        ['Gene9',  0.7,  0.7, 'C1'],
        ['Gene10', 4.9,  0.4, 'C3']
    ]

    # plot(data)
    print distance_matrix(data)

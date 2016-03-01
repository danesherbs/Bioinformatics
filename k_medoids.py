import math
import matplotlib.pyplot as plt
import matplotlib as mpl


def k_medoids(points, k, num_iter=3):
    centres = [ (1.1, 1.9), (2.5, 3.8), (2.45, 2.4) ]
    for _ in xrange(num_iter):
        clusters = _form_clusters(points, centres)
        clusters = _update_clusters_k_medoids(clusters)
        print 'clusters', clusters
    return clusters

def _update_clusters_k_medoids(clusters):
    new_clusters = {}
    for centre in clusters.keys():
        points = clusters[centre]  # points in cluster
        new_centre = _find_centre(points)
        new_clusters[new_centre] = clusters[centre]  # add new
    return new_clusters

def _find_centre(points):
    min_dist = float('inf')
    dist_matrix = distance_matrix(points)
    for index, row in enumerate(dist_matrix):
        cur_dist = sum(row)
        if cur_dist < min_dist:
            min_dist = cur_dist
            centre = points[index]
    return centre

def _form_clusters(points, centres):
    # points  = [ (1.3, 4.2), (3.1, 5.2), (4.2, 5.3) ]
    # centres = [ (1, 1),     (2, 2) ]
    clusters = {}
    for centre in centres:
        clusters[centre] = []
    for point in points:
        min_dist = float('inf')
        for centre in centres:
            cur_dist = _distance(point, centre)
            if cur_dist < min_dist:
                min_dist = cur_dist
                assigned_centre = centre
        clusters[assigned_centre].append(point)  # add point to closest cluster
    return clusters  # {(1, 1): [(1.3, 4.2)], (2, 2): [(3.1, 5.2), (4.2, 5.3)]}

def distance_matrix(points):
    matrix = []
    for point in points:
        point_dists = []
        for other_point in points:
            distance_between = _distance(point, other_point)
            point_dists.append(round(distance_between, 3))
        matrix.append(point_dists)
    return matrix

def _distance(point1, point2):
    dist = 0
    for i in range(len(point1)):
        dist += ( point1[i] - point2[i] ) ** 2
        return math.sqrt(dist)

def plot_data(data):
    xs = [line[1] for line in data]
    ys = [line[2] for line in data]
    plt.plot(xs, ys, '+')
    plt.show()

# def plot_clusters(clusters):
#


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

    points = [ (line[1], line[2]) for line in data ]

    # points  = [ (1.3, 4.2), (3.1, 5.2), (4.2, 5.3) ]
    # centres = [ (1, 1),     (2, 2) ]
    # print _form_clusters(points, centres)

    print k_medoids(points, 3)

    # plot_data(data)

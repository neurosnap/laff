import math
from functools import reduce

def vector_2d(point_one, point_two):
    (x1, y1) = point_one
    (x2, y2) = point_two
    x = calc_vector_slice(x1, x2)
    y = calc_vector_slice(y1, y2)
    return (x, y)

def vector_3d(point_one, point_two):
    (x1, y1, z1) = point_one
    (x2, y2, z2) = point_two
    (x, y) = vector_2d((x1, y1), (x2, y2))
    z = calc_vector_slice(z1, z2)
    return (x, y, z)

def calc_vector_slice(value_one, value_two):
    return value_two - value_one

def add_vectors(vec_x, vec_y):
    return [val + vec_y[i] for i, val in enumerate(vec_x)]

def scale_vector(scale, vector):
    return [(val * scale) for val in vector]

def scaled_addition(scale, vec_x, vec_y):
    scaled_x = scale_vector(scale, vec_x)
    return add_vectors(scaled_x, vec_y)

def transpose_vectors(vec_x, vec_y):
    res = 0
    for i, val in enumerate(vec_x):
        res = res + (val * vec_y[i])
    return res

def euclidean_length(vector):
    dot = transpose_vectors(vector, vector)
    return math.sqrt(dot)

if __name__ == '__main__':
    assert add_vectors((4, -3), (1, 5)) == [5, 2]
    assert add_vectors([-1, 2], [-3, -2]) == [-4, 0]

    print('sum of example vector: ', add_vectors((4, -3), (1, 5)))
    print('sum of vectors: ', add_vectors([-1, 2], [-3, -2]))
    print('sum of vectors: ', add_vectors((-3, -2), (-1, 2)))
    print('sum of vectors: ', add_vectors(add_vectors((-1, 2), (-3, -2)), (1, 2)))

    assert scale_vector(3, (-1, 2)) == [-3, 6]
    assert scale_vector(-0.5, (4, -2)) == [-2.0, 1.0]
    assert scale_vector(0.5, (4, -2)) == [2.0, -1.0]

    print('scale vector: ', scale_vector(3, (-1, 2)))
    print('scale vector: ', scale_vector(2, (4, -2)))
    print('scale vector: ', scale_vector(0.5, (4, -2)))
    print('scale vector: ', scale_vector(-0.5, (4, -2)))

    assert scaled_addition(3, (2, 4, -1, 0), (1, 0, 1, 0)) == [7, 12, -2, 0]
    print('scaled addition: ', scaled_addition(3, (2, 4, -1, 0), (1, 0, 1, 0)))

    assert transpose_vectors((2, 5, -6, 1), (1, 1, 1, 1, 1, 1)) == 2
    assert transpose_vectors((2, 5, -6, 1), (1, 1, 1, 1)) == 2
    vec_1 = add_vectors((2, 5, -6, 1), (1, 2, 3, 4))
    assert transpose_vectors((1, 1, 1, 1), vec_1) == 12

    print('transpose: ', transpose_vectors((2, 5, -6, 1), (1, 1, 1, 1, 1, 1)))
    print('transpose: ', transpose_vectors((2, 5, -6, 1), (1, 1, 1, 1)))
    print('transpose: ', transpose_vectors((1, 1, 1, 1), vec_1))

    assert euclidean_length((1, -2, 2)) == 3.0

    print('euclidean length: ', euclidean_length((1, -2, 2)))

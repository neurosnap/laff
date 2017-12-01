import math
from functools import reduce, partial

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

def dot_product(vec_x, vec_y):
    res = 0
    for i, val in enumerate(vec_x):
        res = res + (val * vec_y[i])
    return res

def euclidean_length(vector):
    dot = dot_product(vector, vector)
    return math.sqrt(dot)

def set_matrix(matrix, value=0):
    columns = len(matrix)
    rows = len(matrix[0])
    return [[value] * rows for _ in range(columns)]

zero_matrix = partial(set_matrix, value=0)
one_matrix = partial(set_matrix, value=1)

def set_to_diagonal(matrix, value=None):
    new_matrix = []
    for i, col in enumerate(matrix):
        new_col = []
        for j, row in enumerate(col):
            val = 0
            if i == j:
                val = value if value else row
            new_col.append(val)
        new_matrix.append(new_col)
    return new_matrix

set_to_identity = partial(set_to_diagonal, value=1)

if __name__ == '__main__':
    assert add_vectors((4, -3), (1, 5)) == [5, 2]
    assert add_vectors([-1, 2], [-3, -2]) == [-4, 0]

    assert scale_vector(3, (-1, 2)) == [-3, 6]
    assert scale_vector(-0.5, (4, -2)) == [-2.0, 1.0]
    assert scale_vector(0.5, (4, -2)) == [2.0, -1.0]

    assert scaled_addition(3, (2, 4, -1, 0), (1, 0, 1, 0)) == [7, 12, -2, 0]

    assert dot_product((2, 5, -6, 1), (1, 1, 1, 1)) == 2
    vec_1 = add_vectors((2, 5, -6, 1), (1, 2, 3, 4))
    assert dot_product((1, 1, 1, 1), vec_1) == 12

    assert euclidean_length((1, -2, 2)) == 3.0

    actual_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    expected_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert zero_matrix(actual_matrix) == expected_matrix

    actual_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    expected_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert one_matrix(actual_matrix) == expected_matrix

    actual_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    expected_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert set_to_identity(actual_matrix) == expected_matrix

    actual_matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    expected_matrix = [[2, 0, 0], [0, 6, 0], [0, 0, 10]]
    assert set_to_diagonal(actual_matrix) == expected_matrix

    print('All tests pass :)')

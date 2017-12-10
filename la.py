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
        res = round(res + val * vec_y[i], 2)
    return res

def euclidean_length(vector):
    dot = dot_product(vector, vector)
    return math.sqrt(dot)

def set_matrix(matrix, value=0):
    rows = len(matrix)
    columns = len(matrix[0])
    return [[value] * columns for _ in range(rows)]

zero_matrix = partial(set_matrix, value=0)
one_matrix = partial(set_matrix, value=1)

def set_to_diagonal(matrix, value=None):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, col in enumerate(row):
            val = 0
            if i == j:
                val = value if value else col
            new_row.append(val)
        new_matrix.append(new_row)
    return new_matrix

set_to_identity = partial(set_to_diagonal, value=1)

def dot_matrix_vector(matrix, vector):
    return [dot_product(row, vector) for row in matrix]

def predict_weather(today, probabilities, days):
    forecast = today
    for _ in range(days - 1):
        forecast = dot_matrix_vector(probabilities, forecast)
    return forecast

def matrix_mult(matrix_one, matrix_two):
    res = []
    col_matrix = row_to_col_matrix(matrix_two)
    for col in col_matrix:
        res.append(dot_matrix_vector(matrix_one, col))
    return row_to_col_matrix(res)

def row_to_col_matrix(matrix):
    new_matrix = [[] for _ in matrix[0]]
    for row in matrix:
        for i, col in enumerate(row):
            new_matrix[i].append(col)
    return new_matrix


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

    matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    vector = [3, 5, 2]
    expected_vector = [29, 59, 89]
    assert dot_matrix_vector(matrix, vector) == expected_vector

    forecast = [[0.4, 0.3, 0.1], [0.4, 0.3, 0.6], [0.2, 0.4, 0.3]]
    weather = dot_matrix_vector(forecast, [0.4, 0.4, 0.2])
    assert weather == [0.3, 0.4, 0.3]

    # print(predict_weather([0.4, 0.4, 0.2], forecast, 2))
    # print(predict_weather([0.3, 0.3, 0.4], forecast, 2))
    # print(predict_weather([0.1, 0.6, 0.3], forecast, 2))

    actual_matrix = row_to_col_matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ])
    expected_matrix = [
        [1, 4, 7, 10],
        [2, 5, 8, 11],
        [3, 6, 9, 12],
    ]
    assert actual_matrix == expected_matrix

    actual_matrix = matrix_mult([
        [0.4, 0.3, 0.1],
        [0.4, 0.3, 0.6],
        [0.2, 0.4, 0.3],
    ], [
        [0.4, 0.3, 0.1],
        [0.4, 0.3, 0.6],
        [0.2, 0.4, 0.3],
    ])
    expected_matrix = [
        [0.3, 0.25, 0.25],
        [0.4, 0.45, 0.4],
        [0.3, 0.3, 0.35],
    ]
    assert actual_matrix == expected_matrix

    matrix_a = [
        [2, 0, 1],
        [-1, 1, 0],
        [1, 3, 1],
        [-1, 1, 1],
    ]
    matrix_b = [
        [2, 1, 2, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    actual_matrix = matrix_mult(matrix_a, matrix_b)
    assert actual_matrix == [
        [5.0, 2.0, 5.0, 2.0],
        [-2.0, 0, -2.0, 0],
        [3.0, 4.0, 3.0, 4.0],
        [-1.0, 0, -1.0, 0.0],
    ]

    actual_matrix = matrix_mult(matrix_b, matrix_a)
    assert actual_matrix == [
        [4, 8, 5],
        [-2, 2, 1],
        [3, 3, 2]
    ]

    print('All tests pass :)')

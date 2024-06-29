def get_matrix(rows, columns, value):
    if rows <= 0 or columns <= 0:
        return []

    matrix = []

    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(value)

        matrix.append(temp)

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


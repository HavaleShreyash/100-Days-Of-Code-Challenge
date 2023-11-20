def rotate(matrix):
    matrix[:] = [x[::-1] for x in list(zip(*matrix))]

if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    rotate(matrix1)
    rotate(matrix2)

    print("Rotated Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nRotated Matrix 2:")
    for row in matrix2:
        print(row)
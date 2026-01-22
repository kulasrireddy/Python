import numpy as np

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nMatrix A:")
    A = create_matrix(rows, cols)

    print("\nMatrix B:")
    B = create_matrix(rows, cols)

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)
    print("\nA + B:\n", A + B)
    print("\nA - B:\n", A - B)
    print("\nA * B (Matrix Multiplication):\n", np.dot(A, B))
    print("\nTranspose of A:\n", A.T)
    print("\nTranspose of B:\n", B.T)

if __name__ == "__main__":
    main()

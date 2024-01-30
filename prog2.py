#Write a program that accepts two matrices A and Bas input and returns their product AB.Check if A & B aremultipliable; if not, return error message.
def mult(a, b, c, r1, c1):
    d = [[0 for _ in range(c1)] for _ in range(c)]
    for i in range(c):  # iterating through column of a
        for j in range(c1):  # iterating through rows of b
            for k in range(r1):
                d[i][j] += a[i][k] * b[k][j]
    return d

if __name__ == "__main__":
    r = int(input("Enter number of rows of matrix 1: "))
    c = int(input("Enter number of columns of matrix 1: "))
    a = []
    for i in range(r):
        b = []
        for j in range(c):
            print(f"Enter element {j + 1} of row {i + 1}")
            b.append(int(input("->")))
        a.append(b)

    r1 = int(input("Enter number of rows of matrix 2: "))
    c1 = int(input("Enter number of columns of matrix 2: "))
    a1 = []
    for i in range(r1):  # Corrected the loop variables
        b = []
        for j in range(c1):
            print(f"Enter element {j + 1} of row {i + 1}")
            b.append(int(input("->")))
        a1.append(b)

    if c == r1:
        print("Product is \n", mult(a, a1, c, r1, c1))  # Corrected the function arguments
    else:
        print("Multiplication is not possible")

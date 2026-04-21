#Evaluate the determinant of a 3x3 matrix.

print("INTERACTIVE MODE - Enter Your Own Matrix")
def determinant_3x3(matrix):
    """
    Formula for 3x3 matrix:
    | a  b  c |
    | d  e  f |
    | g  h  i |
    det = a(ei - fh) - b(di - fg) + c(dh - eg)
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    # det formula
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

def evalute(matrix):
    det = determinant_3x3(matrix)
    print(f"\nDeterminant = {det}")
    print()

own_matrix = []
print("Enter the elements of your 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        value = float(input(f"Enter element [{i + 1}][{j + 1}]: "))
        row.append(value)
    own_matrix.append(row)

evalute(own_matrix)
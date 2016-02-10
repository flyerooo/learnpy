matrix = []
numberOfRaws = eval(input("Enter the number of raw: "))
numberOfColumns = eval((input("Enter the number of columns; ")))
for row in range(numberOfRaws):
    matrix.append([])
    for column in range(numberOfColumns):
        value = eval(input("Enter an elment and press Enter: "))
        matrix[row].append(value)
print(matrix)


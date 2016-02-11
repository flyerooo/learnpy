def find_max_and_min(A):
    min = max = A[0]
    for i in range(1, len(A)):
        if A[i] > max:
            max = A[i]
        elif A[i] < min:
            min = A[i]
    return (min, max)
if __name__ == "__main__":
    # A = [1]
    # A = [1, 2]
    A = [7, 2, 2, 4, 5, 15, 3, 5, 8, 10, 11]
    print(find_max_and_min(A))


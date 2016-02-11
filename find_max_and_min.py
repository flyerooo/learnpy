def find_max_and_min(A):
    len_A = len(A)
    if len_A % 2 == 0:
        begin = 2
        if A[0] > A[1]:
            max, min = A[0], A[1]
        else:
            max,min = A[1], A[0]
    else:
        begin = 1

def sort(lst):
    sortHelper(lst, 0, len(lst) - 1)
def sortHelper(lst, low, high):
    if low < high:
        indexOfMin = low
        min = lst[low]
        for i in range(low + 1, high + 1):
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i
        lst[indexOfMin] = lst[low]
        lst[low] = min
        sortHelper(lst, low + 1, high)

def main():
    lst = [3, 2, 1, 5, 9, 0]
    sort(lst)
    print(lst)
main()
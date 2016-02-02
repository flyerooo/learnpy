def main():
    lst = [1,2,3,4,5]
    reverse(lst)
    for value in lst:
        print(value, end = ' ')
def reverse(lst):
    newLst = len(lst) * [0]

    for i in range(len(lst)):
        newLst[i] = lst[len(lst) - 1 - i]
    lst = newLst

main()
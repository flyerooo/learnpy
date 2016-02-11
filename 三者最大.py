def main():
    n = eval(input("How many numbers are there?"))
    #将第一个值赋给max
    max = eval(input("Enter a number >> "))
    #连续与后面n-1值进行比较
    for i in range(n - 1):
        x = eval(input("Enter a number >> "))
        if x > max:
            max = x
    print("The largest value is", max)
main()
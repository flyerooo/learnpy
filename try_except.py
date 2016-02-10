while True:
    try:
        x=int(input("please enter a number"))
        break
    except ValueError:
        print("Not volid input,try again...")

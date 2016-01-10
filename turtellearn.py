import random

NUMBER_OF_TRIALS = 3000000
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if  x ** 2 + y ** 2 <= 1:
        numberOfHits += 1

pi = 4 * numberOfHits / NUMBER_OF_TRIALS

print("PI is ", pi)

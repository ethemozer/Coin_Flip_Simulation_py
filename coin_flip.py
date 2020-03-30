import random


def flip(num):

    heads = 0
    tails = 0

    for x in range(num):
        result = random.randint(0, 1)
        if result == 0:
            heads += 1
        else:
            tails += 1

    print(f"heads count {heads}")
    print("tails count " + str(tails))


while True:
    try:
        flip(int(input("Please enter a number: ")))
    except:
        print("Invalid number")
    else:
        break

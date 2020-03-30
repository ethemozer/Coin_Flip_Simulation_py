import random


def flip(num):

    heads = 0
    tails = 0

    for x in range(num):
        result = random.randint(0, 1)
        if result == 0:
            heads = heads + 1
        else:
            tails = tails + 1

    print(f"heads count {heads}")
    print("heads count " + str(tails))


while True:
    try:
        user_input = int(input("Please enter a number: "))
        flip(user_input)
    except:
        print("Invalid number")
    else:
        break
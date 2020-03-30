import random

class Flip():

    def __init__(self, num):
        self.num = num

    def flip(self):

        self.heads = 0
        self.tails = 0

        for x in range(self.num):
            result = random.randint(0, 1)
            if result == 0:
                self.heads += 1
            else:
                self.tails += 1

        print("heads: " + str(self.heads))
        print("tails: " + str(self.tails))

    def perc_cal(self):

        heads_percent = self.heads * 100 / self.num
        tails_percent = self.tails * 100 / self.num
        print("heads percent: " + str(heads_percent))
        print(f"tails percent: {tails_percent}")

while True:
    try:
        f = Flip(int(input("Please enter a number: ")))
        f.flip()
        f.perc_cal()
    except:
        print("invalid number")
    else:
        break
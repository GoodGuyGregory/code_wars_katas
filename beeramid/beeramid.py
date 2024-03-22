# kata: https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python

def beeramid(bonus, price):
    levels = 0
    #   drink

    if bonus != 0:
        # still cash in your pocket
        while bonus > 0:
            # subtract the level
            bonus -= ((levels + 1) ** 2) * price
            if bonus >= 0:
                levels += 1
            else:
                # can't afford your tab for this level...
                return levels

        return levels
    else:
        return 0



def main():
    # basic tests:
    print(beeramid(1500, 2)) # should == = 12
    print(beeramid(5000, 3)) # should == = 16


main()
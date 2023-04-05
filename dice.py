import random
def roll_dice():
    roll=input("Roll?? yes or no ")
    while roll.lower()=="Yes".lower():
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)

        print("dice rolled: {} and {}".format(dice1,dice2))
        roll= input("roll again?? yes or no ")
roll_dice()

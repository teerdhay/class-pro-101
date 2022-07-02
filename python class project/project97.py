import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("enter the number between 1-9: "))
    if (introString > number):
        print("Your guess is too large")
    elif (introString == number):
        print("Congratulation! You guessed it correct")
    else :
        print("Your number guess is too less")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You are out of chances")
    
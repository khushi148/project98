import random ;

print(" Number Guessing Game ")

number=random.randint(1,9)

chances=0

print ("enter a number between 1 to 9 ")

while chances < 5:
    que= int (input(" enter a number : "))
    
    if que == number:
        print(" Congartulation !! YOU WON ")

    elif que > number:
        print("Your guess was to high give lower than ",que ) 
    
    else: 
        print("Your GUESS WAS TO LOW give higher than ",que)

    chances= chances+1


if not chances <= 5:
    print("You Lose the game the number is : ", number)



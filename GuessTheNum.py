from random import randint

while True:
    #set / reset the values for the game
    number = randint(1,100)
    trys = 10
    guessing = True

    while guessing == True:
        try:
            #inform the player about the number of tries left 
            guess = int(input(f"Choose a number between 1 and 100 (you have {trys} tries left) "))

            #if the number guessed correctly you win
            if guess == number:
                guessing = False
                print(f"You win, corecct number was {number}")

            #find numbers that are not between 1 and 100 + compensate a try
            elif guess < 1 or guess > 100:
                print("The number must be between 1 and 100")
                trys += 1

            #is the guess higher or lower
            elif guess > number:
                print(f"Lower then {guess}")
            else:
                print(f"Higher then {guess}")

        #find invalid numbers + compensate a try
        except ValueError:
            print("Invalid number")
            trys += 1
        
        #at the end of the turn -1 try
        trys -= 1

    #exit or play again
    if "n" == input("Do you want to play again? [y/n] "):
        exit()

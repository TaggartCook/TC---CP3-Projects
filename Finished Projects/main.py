import random

def main():

    num = 0
    
    diff = input("What difficulty would you like to play? (Easy, Medium, Hard)")

    if diff == "Easy":
        num = random.randint(0,100)

    elif diff == "Medium":
        num = random.randint(0,1000)

    elif diff == "Hard":
        num = random.randint(0,10000)

    elif diff == "XHard":
        num = random.randint(0,100000) 

    elif diff == "XXHard":
        num = random.randint(0,1000000) 
    else:
        print("INVALID RESPONSE")
        main()

    guess = -1
    count = 0

    while guess != num:
        
        guess = int(input("Guess the number!"))

        if guess < num:
            print("Incorrect! (Higher)")
        if guess > num:
            print("Incorrect! (Lower)")
        if guess != num:
            count += 1

    if guess == num:
        print("Correct!")
        print("You got it in",count, "guesses!")

        repeat = input("Would you like to play again? (Yes or No)")
        if repeat == "Yes":
            main()
        if repeat == "No":
            return 0
            
def play():
    main()        
    


play()
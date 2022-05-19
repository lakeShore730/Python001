import random 

'''
Function to guess number
We have used library named ramdom for getting a randam number every time when this function is called.
'''

def guess_number(x):
    random_number = random.randint(1, x)
    guess_num = 0
    
    while guess_num != random_number:
        guess_num = int(input(f"Guess a number between 1 and {x}: "))
        if guess_num < random_number: 
            print("Sorry, guess again. Too low.")
        elif guess_num > random_number:
            print("Sorry, guess again> Too high.")

    print(f"Yay, congrares. You have guessed the number ({guess_num}).")


'''
 Function to gusess number by computer 

'''

def guess_computer(high_num):
    low = 1
    high = high_num
    feedback= ""

    while feedback != "c":
        if low < high:
            guess = random.randint(low, high)
        else: 
            guess = low

        feedback = input(f"Is {guess} too high  (H), too low (L), or correct (c) : ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay, congrares computer. You have guessed the number")
    

guess_computer(20)
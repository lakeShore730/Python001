import random 
import string
from dataset.word_list import word_list

# Function to get valid random word

def get_valid_word(words):
    word = random.choice(words)
    
    # Select new word if the selected word contains space or hyphon (-).
    
    while "-" in word or " " in word: 
        word = random.choice(words)
    return word    


def human():
    word = get_valid_word(word_list)
    word_letters = set(word.upper())    
    alphabet = set(string.ascii_uppercase) # Get A to Z chars (with uppercase ascending order) in string format and convent them to the set.
    used_letters = set() # what user has guessed word 

    count = len(word)

    while len(word_letters) > 0 and not count == 0 :
        print("You have ", count, "live")
        count -= 1
        # print all used letters 
        if(len(used_letters)):
            print("You have already used these letters : ", " ".join(used_letters))

        # let's show what used have guessed 
        word_with_guess = [letter if letter in used_letters else "_" for letter in word.upper()]  
        print(" ".join(word_with_guess))  
        
        # getting user input (char)
        user_letter = input("Guess a letters : ").upper()
        
        if user_letter in alphabet - used_letters: # check if user has already guessed/added this char
            used_letters.add(user_letter)
            
            if user_letter in word_letters: 
                word_letters.remove(user_letter) # remove the char after guessing the correct char 
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
            
        else:
            print("Invalid character. Please try again.")
    
    if not len(word_letters):
        print("Congrats, you guessed the word successfully")
        
    else: 
        print("Sorry, mession incomplete....")
           
human()


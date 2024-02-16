#Import of PyDictionary module
from PyDictionary import PyDictionary

#Assigns PyDictionary to a variable
dictionary = PyDictionary()

#Dictionary with letter keys with their associated values
letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, 
           "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, 
           "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, 
           "P": 3, "Q": 10,"R": 1, "S": 1, "T": 1, 
           "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
           "Z": 10}

#Initialized an empty dictionary for the scoreboard
score_board = {}

#Initialized the total for the total points
total = 0
#Menu function displaying information
def menu():
    print("Welcome to Scrabble the game!")
    print("Press 1 to exit...")

#The main function that calls all the other functions
#It also prints most if not all of the outputs
def main():
    menu()
    while True:
        #A try and except to catch any exceptions
        try:
            #Getting the word from the user
            user_input = input("Please enter a word: ").upper()
            #Breaks the loop if the user enters "1"
            if user_input == "1":
                break
            if is_word_real(user_input):
                score_counter(user_input)
                print("--------")
                for key, value in score_board.items():
                    print(f"{key}: {value}")
                print("--------")
                print(f"Total score: {total_score(total)}")
                print("--------")
        #Catches any words that are not real words
        except:
            print("Please enter a word!")

#A function to check if a word is real or not
def is_word_real(word):
    #Try and excepts that returns True if a meaning is returned
    try:
        return bool(dictionary.meaning(word))
    #Exception that returns False if the .meaning(word) returns "None"
    except:
        return False

#A function to count the score of a word
def score_counter(word):
    score = 0
    #For loop to add up the points of each letter
    for letter in word:
        score += letters.get(letter)
    #Adds the word and its score to the scoreboard
    score_board[word] = score

#A function to calculate the total points by adding up all the scores
def total_score(total):
    #For loop that adds the values of the scoreboard dictionary 
    for value in score_board.values():
        total += value
    return total

#Condtion that only calls the main function if this is the main file
if __name__ == "__main__":
    main()
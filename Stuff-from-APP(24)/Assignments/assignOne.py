# In the game of Scrabble™, each letter has points associated with it. The total score
# of a word is the sum of the scores of its letters. More common letters are worth fewer
# points while less common letters are worth more points. The points associated with


# each letter are shown below:
# One point A, E, I, L, N, O, R, S, T and U
# Two points D and G
# Three points B, C, M and P
# Four points F, H, V, W and Y
# Five points K
# Eight points J and X
# Ten points Q and Z

# Write a program that computes and displays the Scrabble™ score for a word.
# Create a dictionary that maps from letters to point values. Then use the dictionary to
# compute the score.



from PyDictionary import PyDictionary

dictionary = PyDictionary()

letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, 
           "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, 
           "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

score_board = {}

total = 0
def menu():
    print("Welcome to the Scrabble the game!")
    print("Press 1 to exit...")

def main():
    menu()
    while True:
        try:
            print("--------")
            for key, value in score_board.items():
                print(f"{key}: {value}")
            print("--------")
            user_input = input("Please enter a word: ").upper()
            if is_word_real(user_input):
                score_counter(user_input)
                print(total_score(total))
        except:
            print("Please enter a word!")

def is_word_real(word):
    try:
        return bool(dictionary.meaning(word))
    except:
        return False
    
def score_counter(word):
    score = 0
    for letter in word:
        score += letters.get(letter)
    score_board[word] = score
def total_score(total):
    for value in score_board.values():
        total += value
    return total

if __name__ == "__main__":
    main()
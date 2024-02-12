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
# A Scrabble™ board includes some squares that multiply the value of a letter
# or the value of an entire word. We will ignore these squares in this exercise.


from PyDictionary import PyDictionary
dictionary = PyDictionary()

def is_word_real(word):
    try:
        return bool (dictionary.meaning(word))
    except:
        return False

letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, 
           "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, 
           "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
def main():
    user_input = input("Please enter a word: ").upper()
    if is_word_real(user_input):
        score = 0
        for letter in user_input:
            score += letters.get(letter)
        print(f"Your score is {score}")
if __name__ == "__main__":
    main()
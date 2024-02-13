from PyDictionary import PyDictionary

dictionary = PyDictionary()

letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, 
           "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, 
           "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, 
           "P": 3, "Q": 10,"R": 1, "S": 1, "T": 1, 
           "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
           "Z": 10}

score_board = {}

total = 0
def menu():
    print("Welcome to Scrabble the game!")
    print("Press 1 to exit...")

def main():
    menu()
    while True:
        try:
            user_input = input("Please enter a word: ").upper()
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
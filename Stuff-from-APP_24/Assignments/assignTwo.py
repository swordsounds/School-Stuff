#This is the functuon to check if word is a palindrome
def palindromeCheck(string):
    #Base case
    if len(string) == 0:
        return "is a palindrome"
    #Condition to check the first and last letter
    elif string[0] == string[-1]:
        #Recursive step that checkpoints the letters inbetween what was already checked
        #To then make the first and last letter of that, to then be checked, so on and so forth
        return palindromeCheck(string[1:-1])
    else:
        return "not a palindrome"
    
#-----------------TEST CODE-------------------
# strings = ["kayak", "taco cat", "racecar", 
#          "never odd or even", 
#          "step on no pets", "ufo tofu"]

# for string in strings:
#     if palindromeCheck(string.replace(" ", "")):
#         print(string, "is a palindrome")
#     else:
#         print(string, "is not a palindrome")
#---------------------------------------------
    
#Conditon to run if this is the main file
if __name__ == "__main__":
    #Prints whatever is returned from the function as it is called
    print(palindromeCheck(input("Enter a word: ").replace(" ", "").lower()))
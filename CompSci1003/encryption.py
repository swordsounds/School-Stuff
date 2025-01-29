# encryption using a linear feedback shift register
import bindec

b64_alphabet = {
        'A': 0, 'B': 1, 'C': 2,
        'D': 3, 'E': 4, 'F': 5,
        'G': 6, 'H': 7, 'I': 8,
        'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14, 
        'P': 15, 'Q': 16, 'R': 17,
        'S': 18, 'T': 19, 'U': 20,
        'V': 21, 'W': 22, 'X': 23,
        'Y': 24, 'Z': 25,

        'a': 26, 'b': 27, 'c': 28, 
        'd': 29, 'e': 30, 'f': 31,
        'g': 32, 'h': 33, 'i': 34, 
        'j': 35, 'k': 36, 'l': 37, 
        'm': 38, 'n': 39, 'o': 40, 
        'p': 41, 'q': 42, 'r': 43, 
        's': 44, 't': 45, 'u': 46, 
        'v': 47, 'w': 48, 'x': 49, 
        'y': 50, 'z': 51, '0': 52, 
        '1': 53, '2': 54, '3': 55,
        '4': 56, '5': 57, '6': 58, 
        '7': 59, '8': 60, '9': 61, 
        '+': 62, '/': 63
    }

# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c):
    # Implement me
    temp = []
    for l in bindec.decToBin(b64_alphabet[c]):
      temp.append(l)  
    return temp

# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b):
    deci = bindec.binToDec(b)
    ret = list(
        b64_alphabet.keys()
        )[list(
            b64_alphabet.values()
            ).index(deci)]
    return ret


# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(s):
    # Implement me
    temp = []
    chars = [charToBin(l) for l in s]
    for i in chars:
        for j in i:
            temp.append(j)
    return temp

# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    # Implement me
    start = 0
    end = 6
    string = ''
    while True:
        if end >= len(b_list) + 1:
            break
        chars = binToChar(b_list[start:end])
        string+=chars
        start = end
        end+=6
    return string

# generates a sequence of pseudo-random numbers
def generatePad(seed, k, length):
    # Implement me
    temp = []

    for i in range(0, length):
        a=seed[0]
        b=seed[-k]
        xor=a^b
        seed = seed[1:]
        seed.append(xor)
        temp.append(str(xor))
    return temp

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    # Implement me
    temp = []
    binary = strToBin(message)
    one_time_pad = generatePad(seed, k, len(message)*6) 

    for i in range(0, len(binary)):
        a=int(binary[i])
        b=int(one_time_pad[i])
        xor=a^b
        temp.append(xor)
        
    return binToStr(temp)
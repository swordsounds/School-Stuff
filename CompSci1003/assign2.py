# Question 1
# Returns all permutations of a set
# Modify this to generate the set as on slide 18 of Topic 2
def permutations(aSet):
  if len(aSet) <= 1: 
    return aSet

  all_perms = []

  first_element = aSet[0:1]
  subset = aSet[1:]

  partial = permutations(subset)
  for permutation in partial:
    for index in range(len(aSet)):
      new_perm = list(permutation[:index])
      new_perm.extend(first_element)
      new_perm.extend(permutation[index:])
      all_perms.append(new_perm)

  return all_perms


# Question 2
# Given 'n' as input, generate a list of numbers from 2^n-1 down to 0
def generateReverseOrder(n):
  # Implement me!
  if not n:
      return

  for i in range(2**n):
      s = bin(i)[2:]
      s = "0" * (n - len(s)) + s
      yield s
  return []


# Question 3
# Return a 3-element integer list containing number of consonants, vowels,
# and other characters (respectively) for the given string



def countChars(s, score=[0,0,0]):
  # Implement me!
  vowels = ['a', 'e', 'i', 'o', 'u']
  consonants = ['b','c','d','f','g','h','j','k','l','m','n','p',
                'q','r','s','t','v','w','x','y','z']
  other = [' ']

  if len(s) <= 1:
    return s
  

  firstEl = s[0:1]
  lastEl = countChars(s[1:])

  if firstEl in vowels:
    score[1] += 1
  if firstEl in other:
    score[2] += 1
  if lastEl in vowels:
    score[1] += 1
  if firstEl in consonants:
    score[0] += 1
  return score


# --------------------------------------------------------
# Tester code for all questions
# Q1 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q1 tester\n")
print("Actual:  ", end=' ')
for permutation in permutations(["d","o","g"]):
  print(permutation, end=' ')
print("\nExpected:", end=' ')
print("['d', 'o', 'g']", end=' ')
print("['d', 'g', 'o']", end=' ')
print("['o', 'd', 'g']", end=' ')
print("['o', 'g', 'd']", end=' ')
print("['g', 'd', 'o']", end=' ')
print("['g', 'o', 'd']")


# Q2 tester code; do not make any changes to this block of code
print("------------------------------------------------")
print("Q2 tester\n")
print("Descending binary numbers:")
for i in range(1, 5):
  print(i, "bit:", *generateReverseOrder(i))

print("\nExpected:")
print("1 bit: 1 0")
print("2 bit: 11 10 01 00")
print("3 bit: 111 110 101 100 011 010 001 000")
print("4 bit: 1111 1110 1101 1100 1011 1010 1001 1000 0111 0110 0101 0100 0011 0010 0001 0000")


# Q3 tester code; you may make changes to the call to countChars(),
# to account for any extra parameters you may add
print("------------------------------------------------")
print("Q3 tester\n")
s = "abc de"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [3, 2, 1]")
print()
s = "To be or not to be"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [7, 6, 5]")

print("------------------------------------------------")

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
  for index in range(len(aSet)):
    for permutation in partial:
      new_perm = list(permutation[:index])
      new_perm.extend(first_element)
      new_perm.extend(permutation[index:])
      all_perms.append(new_perm)

  return all_perms


# Question 2
# Given 'n' as input, generate a list of numbers from 2^n-1 down to 0
def generateReverseOrder(n):
  # Implement me!
  if n == 0:
    return ['']
  
  nextIter = generateReverseOrder(n-1)
  
  ret = []
  
  for bin in nextIter:
    ret.append(bin + '1')
    ret.append(bin + '0')
    
  return ret


# Question 3
# Return a 3-element integer list containing number of consonants, vowels,
# and other characters (respectively) for the given string
def countChars(s,c=0,v=0,o=0):
  # Implement me!
  if len(s) == 0:
    return [c, v, o]
    
  if s[0].lower() in 'aeiou':
    v += 1
  elif s[0].lower() in 'bcdfghjklmnpqrstvwxyz':  
    c += 1
  elif not s[0].lower().isalpha():
    o += 1  
  
  return countChars(s[1:], c, v, o)


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

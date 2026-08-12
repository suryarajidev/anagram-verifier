# Anagram checker

string1 = input("give me a word:  ")
string2 = input("give me an anagram of such word:  ")

def count_letters(string):
  letters = {}
  for char in string:

    works = True
    try:
      letters[char]
    except:
      works = False

    if works:
      letters[char] += 1
    else:
      letters[char] = 1

  return letters

dict1 = count_letters(string1)
dict2 = count_letters(string2)

print(dict1)
print(dict2)

if dict1 == dict2:
  print("they are anagrams")
else:
  print("they aren't anagrams")

__author__ = 'tocando'

import scrabble

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

def has_all_vowels(word):
    for word in scrabble.wordlist:
        return word


x = 0
while x < 10:
    ba = has_all_vowels(word)
    print('the word is ', ba)
    x = x + 1
#for word in scrabble.wordlist:
 #   for x in range(0, 10):
  #      print(word)

#word_with_all_vowels = has_all_vowels()
#print('word_with_all_vowels is : ', word_with_all_vowels)

#for letter in letters:
#    if not has_a_double(letter):
#        print(letter + " never occures as a double")

# Print all words containing 'uu'
#for word in scrabble.wordlist:
#    if 'uu' in word:
#        print(word)

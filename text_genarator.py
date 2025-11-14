#mummber of word
#mummber of unique word
#mummber of to be verbs
#total mummber of 'to be' occurrences
from pygments.lexer import words

text = ("The sound of the waves crashing against the shore was both calming and invigorating"
        "The salty breeze blew through her hair "
        "and she felt the warmth of the sun on her skin"
        "She closed her eyes and took a deep breath feeling grateful to be alive in this moment"
        "I am 38 I was in Turkey last year We were happy there also "
        "Weather is perfect and sun is beautiful"
        "my family are there yet")

word = text.split()
word_set = set(word)
toBe = {'am', 'is', 'are', 'was', 'were'}



print(toBe.intersection(word_set))
print(len(word))
print(len(word_set))

print(sum(1 for w in word if w in toBe))
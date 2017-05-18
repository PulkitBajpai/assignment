__author__ = 'pulkit-bajpai'

from cleanwords import cleanswords

with open("file2.txt") as f:
     wordstring = f.read()

word_list = cleanswords(wordstring)

word_freq = []
for w in word_list:
    word_freq.append(word_list.count(w))

print word_list
print word_freq
print(zip(word_list, word_freq))
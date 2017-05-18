__author__ = 'pulkit-bajpai'

from cleanwords import cleanswords

with open("file2.txt") as f:
     wordstring = f.read()

word_list = cleanswords(wordstring)

word_freq = []
for w in word_list:
    word_freq.append(word_list.count(w))

print word_list
print(zip(word_list, word_freq))

with open("file2.txt") as f:
     noise_tring = f.read()

noise_words_list = noise_tring.split()
final_result = []
for word in word_list:
    if not word in noise_words_list:
        final_result.append(word)
print final_result

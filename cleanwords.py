__author__ = 'pulkit-bajpai'
# local change

# 1) Write a function getwords(text) to take a string, parse it and return words (tokens)
text = "123te A git repo, upload these tasks as you finish each task and send the url of that repo"
# def getwords(data):
#     return data.split()
#
# words_list = getwords(text)
# print words_list

# 2) cleanwords.py -  Modify getwords and call it cleanwords(text). Cleanwords removes punctuation,
#    removes words which are just numbers, convert all words to lower case and return them.

import re

def cleanswords(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    #remove punctuations

    without_punct=""
    for cha in text:
       if cha not in punctuations:
             without_punct += cha.lower()

    print without_punct
    without_number = re.sub(r'\b[0-9]+\b\s*', '', without_punct)
    word_list = re.sub(r'\w*\d\w*', '', without_number).strip()
    word_list = word_list.split()
    return word_list

clean_words = cleanswords(text)
print clean_words


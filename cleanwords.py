__author__ = 'pulkit-bajpai'


#1) Write a function getwords(text) to take a string, parse it and return words (tokens)
text = "123te A git repo, upload these tasks as you finish each task and send the url of that repo"
def getwords(data):
    return data.split()

words_list = getwords(text)
print words_list


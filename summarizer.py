'''
Created on Mar 27, 2019

@author: nsno
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import urllib2
response = urllib2.urlopen('http://python.org/')
text = response.read()
stopWords = set(stopwords.words('english'))
words = word_tokenize(text)
freq = dict()
for word in words:
    if word in stopWords:
        continue
    elif word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sentences = sent_tokenize(text)
sentence_score = dict()
for sentence in sentences:
    score,wordcount = 0
    for word,num in freq.items():
        if word in sentence.lower():
            score += num
            wordcount+=1
    sentence_score[sentence] = score/wordcount
count = 0
sumofscores = 0
for x in sentence_score.values():
    sumofscores+=x
    count+=1
summary = ""
for sentence,score in sentence_score.items():
    if score>1.5*(sumofscores/count):
        summary+=" "+sentence
print("SUMMARY:-\n%s",summary)
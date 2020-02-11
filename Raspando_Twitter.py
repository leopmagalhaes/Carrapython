#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:06:31 2019

@author: usuario
"""
from twython import Twython
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

ConsumerKey = "UyE3napIHPj7baj9KXZKmZhoS"
ConsumerSecret = "4elSNHHrRzplKpw5vz6nngS5SBxjlkn9zwkg7QulMzoWkvUWmi"
AccessToken = "878764721398325250-WTf4KUK3tlV2J5iNXVHtuFZ5qyvcvZs"
AccessTokenSecret = "nZXkr2owl73BCjpAzNeCOGAnvAAa7BTaq4UFAQmFmH7UK"

twitter = Twython(ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret)



Busca = input("Digite a palavra a ser pesquisada: ")

result = twitter.search(q=Busca)
tweet = []

for status in result["statuses"]:
    print("USUARIO: {0}.\n TWEET: {1}.\n HORARIO DA POSTAGEM: {2}".format(status["user"]["name"], status["text"], status["created_at"]))
    with open('tweet.csv', 'a') as f:
        f.write("{0}.\n".format(status["text"]))
        

from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from unidecode import unidecode

text = open('tweet.csv','r').read()
#text = unidecode(texto)
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(text)
palavras = word_tokenize(text.lower())

from nltk.corpus import stopwords
from string import punctuation
stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

#from collections import Counter
#palavras = text2.replace('\n',' ').replace('\t','').split(' ')
#contador = Counter(palavras)

from nltk.probability import FreqDist
from heapq import nlargest
frequencia = FreqDist(palavras_sem_stopwords)
idx_palavras_importantes = nlargest(4, frequencia, frequencia.get)

#for i in contador.items():
 #   print i
from collections import defaultdict
sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

from heapq import nlargest
idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)


nuvem = WordCloud(max_font_size=100,width = 1520, height = 535).generate(text)
plt.figure(figsize=(16,9))
plt.imshow(nuvem)
plt.axis("off")
plt.show()

print(idx_palavras_importantes)
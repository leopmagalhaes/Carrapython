#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:51:10 2019

@author: usuario
"""

import pandas as pd
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_excel('sentiment_analysis.xlsx')
df.head()

from translate import Translator

for index, row in df.iterrows():
    en_blob = df.iloc[index]['Frase']
    sentiment = df.iloc[index]['Sentimento']
    translator= Translator(to_lang="pt")
    pt_blob = translator.translate(en_blob)
    df.at[index, str('Frase')] = str(pt_blob)
    df.at[index, str('Sentimento')] = sentiment
df.head()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

vetorizador = CountVectorizer(binary = 'true')
X = vetorizador.fit_transform(df['Frase'])

y = df.Sentimento

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = BernoulliNB()
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
y_true =  y_test

print("Resultados obtidos: ")
print(y_pred)
print("\n Resultados esperados: ")
print(y_true.values)

from sklearn import metrics

print("Precision Macro " + str(metrics.precision_score(y_true, y_pred, average='macro')))
print("Precision Micro " + str(metrics.precision_score(y_true, y_pred, average='micro')))
print("Precision Weighted " + str(metrics.precision_score(y_true, y_pred, average='weighted')))


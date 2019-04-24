# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df = pd.read_csv('world-cities.csv')
pl = df.iloc[:,0]       #Places Dataset
places = []
for w in pl:
	places.append(w)

import nltk
from nltk.corpus import names as nm
names = nm.words('male.txt')
for w in nm.words('female.txt'):
    names.append(w)
names_filtered = []
for w in names:
    if w not in names_filtered:
        names_filtered.append(w)    #Names Dataset

f = open('animals.txt')
animals = f.read().split('\n')

df1 = pd.read_csv('things.csv')
thi = df1.iloc[:, 1]         #Things Dataset
things = []
for w in thi:
	things.append(w)

used_names = []
used_places = []
used_things = []
used_animals = []
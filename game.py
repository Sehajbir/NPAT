#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:57:51 2019

@author: sehaj
"""
from data import *
import string
import random
import re
from gtts import gTTS
import os
def run(ch):
    name_re = r'^'+re.escape(ch)+r''
    for w in names_filtered:
        if re.match(name_re, w, re.I):
            if w not in used_names:
                print(w)
                myobj = gTTS(text = w, lang = 'en', slow=False)
                myobj.save("name.mp3")
                os.system("mpg321 name.mp3")
                used_names.append(w)
                break
    place_re = r'^'+re.escape(ch)+r''
    for w in places:
        if re.match(place_re, w, re.I):
            if w not in used_places:
                print(w)
                myobj = gTTS(text = w, lang = 'en', slow = False)
                myobj.save("place.mp3")
                os.system("mpg321 place.mp3")
                used_places.append(w)
                break
    animal_re = r'^'+re.escape(ch)+r''
    for w in animals:
        if re.match(place_re, w, re.I):
            if w not in used_animals:
                print(w)
                myobj = gTTS(text = w, lang = 'en', slow = False)
                myobj.save("animal.mp3")
                os.system("mpg321 animal.mp3")
                used_animals.append(w)
                break
    things_re = r'^'+re.escape(ch)+r''
    for w in things:
        if re.match(things_re, w, re.I):
            if w not in used_things:
                print(w)
                myobj = gTTS(text = w, lang = 'en', slow = False)
                myobj.save("thing.mp3")
                os.system("mpg321 thing.mp3")
                used_things.append(w)
                break
    print('\n')
    return

used_names = []
used_places = []
used_things = []
used_animals = []

for i in range(1):
    ch = random.choice(string.ascii_letters)
    run(ch)

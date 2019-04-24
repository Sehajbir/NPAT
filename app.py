from flask import Flask, render_template, request
app = Flask(__name__)
from data import *
import string
import random
import re

fnames = names_filtered
fanimals = animals
fplaces = places
fthings = things
@app.route('/')
def index_view():
	return render_template('index.html')
@app.route('/game')
def game_view():
	ch = random.choice(string.ascii_letters)
	name_re = r'^'+re.escape(ch)+r''
	for w in names_filtered:
		if re.match(name_re, w, re.I):
			if w not in used_names:
				nm = w
				used_names.append(w)
				break
			else:
				nm = 'Not Found'
	place_re = r'^'+re.escape(ch)+r''
	for w in places:
		if re.match(place_re, w, re.I):
			if w not in used_places:
				pl = w
				used_places.append(w)
				break
			else:
				pl = 'Not Found'
	animals_re = r'^'+re.escape(ch)+r''
	for w in animals:
		if re.match(animals_re, w, re.I):
			if w not in used_animals:
				an = w
				used_animals.append(w)
				break
			else:
				an = 'Not Found'
	things_re = r'^'+re.escape(ch)+r''
	for w in things:
		if re.match(things_re, w, re.I):
			if w not in used_things:
				th = w
				used_things.append(w)
				break
			else:
				th = 'Not Found'
	return render_template('game.html', ch = ch.upper(), name = nm, place = pl, animal = an, thing = th.title())

@app.route('/user')
def userview():
	ch = random.choice(string.ascii_letters)
	return render_template('user.html', ch = ch.upper())

@app.route('/eval', methods = ['POST', 'GET'])
def eval():
	if request.method == "POST":
		result = request.form
		ch = result["choice"]
		nm = result["name"]
		pl = result["place"]
		an = result["animal"]
		th = result["thing"]
		count = 0
		rec = r'' + re.escape(ch) + r''
		if re.match(rec, nm, re.I):
			count = count + 1
		if re.match(rec, pl, re.I):
			count = count + 1
		if re.match(rec, an, re.I):
			count = count + 1
		if re.match(rec, th, re.I):
			count = count + 1
		if nm in fnames:
			count = count + 1
		
		if pl in fplaces:
			count = count + 1
		
		if an in fanimals:
			count = count + 1
		
		if th.lower() in fthings:
			count = count + 1
		
		if count == 8:
			return render_template('evalSuccess.html')
		else:
			return render_template('evalFailure.html')
if __name__ == '__main__':
	app.run()

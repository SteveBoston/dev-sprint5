# This is whre you can start you python file for your week1 web app
# Name: Steve Gallagher

import flask, flask.views
import os
import utils
import itertools



class Scrabble(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('scrabble.html')


	@utils.login_required
	def post(self):
		q = flask.request.form["wordlist"]
		x = flask.request.form["wordlength"]
		y = int(x)
		result = scrabble_words(q,y)
		flask.flash(result)
		return flask.redirect(flask.url_for('scrabble'))




def checker(string, a):                      #Take a string and an empty list. Returns the list filled with all possible letter combinations
	if len(string) > 1:						 # whose lengths are less than the original string
		n = 0
		num = len(string) - 1
		while n < num + 1:
			b = []
			e = string[0:n] + string[n + 1:num + 1]
			b.append(e)
			a.append(e)
			n = n + 1
			for i in b:
				checker(i,a)
	return a

def reducer(string):						#Takes a string and passes it into the checker function, and then strips out redundant elements return in the 
	a = []									# checker list
	y = []
	z = checker(string, a)
	for i in z:
		if i in y:
			pass
		elif i not in y:
			y.append(i)
	return y


def word_finder(string):					#Takes a string and looks through the file words.txt to see if the letters in the string can be used
	fin1 = open("words.txt")				# to form any words with the same number of letters.
	h = []
	for line in fin1:
		word1 = line.strip()
		if sorted(string) == sorted(word1):
			h.append(word1)
	return h


def scrabble_words(wordlist, lettercount):        #Takes a list of letters and a word length and returns words that match
	if lettercount == len(wordlist):
		j = word_finder(wordlist)
		if j == []:
			return "Sorry, the word list has no words with that length and combination of letters."	
		else:
			return "You can make the words",j
	if lettercount > len(wordlist):
		return "The word length you chose is too long. Your maximum word length is", len(wordlist),"letters. You submitted", lettercount
	elif lettercount < len(wordlist):
		j = reducer(wordlist)
		k = []
		for i in j:
			if len(i) == lettercount:
				k.append(i)
		l = []
		for i in k:
			m = word_finder(i)
			if m != [] and m not in l:
				l.append(m)

		l = list(itertools.chain.from_iterable(l))
	

		if l == []:
			return "Sorry, the word list has no words with that length and combination of letters."	
		else:
			return "You can make the words:", l



# def scrabble_words(wordlist, lettercount):        #Takes a list of letters and a word length and returns words that match
# 	if lettercount == len(wordlist):
# 		j = word_finder(wordlist)
# 		if j == []:
# 			print "Sorry, the word list has no words with that length and combination of letters."	
# 		else:
# 			print "You can make the words",j
# 	if lettercount > len(wordlist):
# 		print "The word length you chose is too long. Your maximum word length is", len(wordlist),"letters."
# 	elif lettercount < len(wordlist):
# 		j = reducer(wordlist)
# 		k = []
# 		for i in j:
# 			if len(i) == lettercount:
# 				k.append(i)
# 		l = []
# 		for i in k:
# 			m = word_finder(i)
# 			if m != []:
# 				l.append(m)

# 		l = list(itertools.chain.from_iterable(l))

# 		if l == []:
# 			print "Sorry, the word list has no words with that length and combination of letters."	
# 		else:
# 			print "You can make the words",l
# 	
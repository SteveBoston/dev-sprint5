# Ch. 13
# Steve Gallagher


import string
import random


fin = open("TomSawyer.txt")


b = []

for line in fin:
	l = line.split(" ")
	for word in l:
		b.append(word)


c = []

for word in b:
	word = word.strip()
	word = word.lower()
	word = word.strip(string.punctuation)
	c.append(word)


c = filter(None, c)

# need to add something to split words connected with --

def word_mapper(li,d,n,prefix_length):
	h = prefix_length
	x = li[n:n + h]
	a = tuple(x)
	b = li[n + h]
	if a not in d:
		c = []
		c.append(b)
		d[a] = c
	else:
		d[a].append(b)
	return n, d
	


def iterate(li, prefix_length):
	d = {}
	n = 0
	z = prefix_length
	while n < len(li) -z:
		word_mapper(li,d,n,prefix_length)
		n = n + 1
	return d





def markov_text(li, word_num, prefix_length):
	dic = iterate(li, prefix_length)
	temp1 = random.choice(dic.keys())  
	temp = list(temp1)               
	n = 0
	q = temp1
	def repeat(dic, temp, n, q, word_num):
		a = dic[q]
		z = prefix_length
		# print "the prefix is", z
		# print q
		# print a
		if n < word_num:
			b = random.choice(a)
			temp.append(b)
			q = tuple(temp[-z:])
			n = n + 1
			# print "iteration", n
			repeat(dic, temp, n, q, word_num)

		return temp

	repeat(dic, temp, n, q, word_num)

	delimeter = " "
	text = delimeter.join(temp)

	return text



print markov_text(c, 25, 3)  #first parameter is the list formed by the book words, second is length of markov text to be generated, third is prefix length


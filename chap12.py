# Ch. 12 
# Steve Gallagher
	
	
def checker(string):
	fin1 = open("words.txt")
	b = {}
	e = []
	for line in fin1:
		word1 = line.strip()
		if sorted(string) == sorted(word1) and string != word1:
			e.append(word1)
	b[string] = e
	if e != []:
		 return b
	else:
		return None
	


def placeholder():
	return None


def anagrams():
	fin = open("words.txt")
	d = {}
	n = 0

	for line in fin:
		word = line.strip()
		if n <= 93000:
			a = placeholder()
			n = n + 1
			if n%3000 == 0:
				print n
				print d
			if a != None:
				d.update(a)
		else:
			a = checker(word)
			n = n + 1
			if n%3000 == 0:
				print n
				print d
			if a != None:
				d.update(a)
			
	return d

		
# print checker("deltas")

# print checker("aa")

print anagrams()


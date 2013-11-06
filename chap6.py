# Enter your answrs for chapter 6 here
# Name: Steve Gallagher


# Ex. 6.6

def first(word, z):
	return word[z]

def last(word, z):
	return word[-z]


def is_palindrome(word):

	a = 0
	b = 1

	c = len(word)
	print "length of word is", c
	if c % 2 == 0:
		c = c
	else:
		c = c-1

	n = len(word)
	if n % 2 == 0:
		n = n
	else:
		n = n-1
	print "initial value for n is", n	

	def checker(word, a, b, c, n):
			if c/2 > n:
				print "yes, this word is a palindrome"  

			else:
				if first(word, a) != last(word, b):
					print "RECURSE", n
					print "value for a is", a, "which is", first(word, a)
					print "value for b is", b, "which is", last(word, b)
					print "no, this word is not a palindrome"
				else:
					print "RECURSE", n
					print "a is", a, "which is", first(word, a)
					print "b is", b, "which is", last(word, b)
					checker(word, (a+1), (b+1), c, (n-1))


	checker(word, a, b, c, n)

is_palindrome('redikutgcjhgider')



# Ex 6.8


def gcd(a,b):

	if b == 0:
		print "The greatest common divisor is", a

	else:
		r = a % b
		a = b
		b = r

		gcd(a,b)



#gcd(100,12)








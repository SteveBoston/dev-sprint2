# Enter your answrs for chapter 7 here
# Name: Stephen Gallagher


from __future__ import division


import math


# Ex. 7.5


def estimate_pi():

	k = 0

	term = 0

	x = 2*math.sqrt(2)/9801

	def iterate(k, x, term):

		print "ITERATION"
		
		a = math.factorial(4*k)*(1103+(26390*k))

		b = (math.factorial(k)**4)*(396**(4*k))

		term =  term + a/b
		
		if a/b < 1e-15:
			print "function estimate of pi is", 1/(x * term)

		else: 

			k = k + 1

			iterate(k, x, term)	
		
	iterate(k, x, term)
	
estimate_pi()


# How many iterations does it take to converge?    4 Iterations

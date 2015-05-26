#!/usr/bin/env python
#coding=utf8


def decorator(F):
	def new_sum(a,b):
		print "input: ",a, b
		return F(a,b)
	return new_sum




@decorator 
def square_sum(a,b):
	return a**2 + b**2

@decorator
def suare_diff(a,b):
	return a**2 - b**2


print square_sum(3,6)
print suare_diff(3,6)


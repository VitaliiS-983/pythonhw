#!/usr/bin/python

def reverse(s):
	str = ""
	for i in s:
	  str = i + str
	return str
s = "I am testing"

print "Reverse sentence:",(reverse(s))

#!/usr/bin/python
## Prime
# Takes an input and return all primes up to input
# prime.py script
# Source Code produced by Willtech 2023
# v0.1 hand coded by HRjJ

#prime.py [number to check] []

## setup dependencies
import sys
import re

import mpmath
#@manual{mpmath,
#  key     = {mpmath},
#  author  = {The mpmath development team},
#  title   = {mpmath: a {P}ython library for arbitrary-precision floating-point arithmetic (version 1.3.0)},
#  note    = {{\tt http://mpmath.org/}},
#  year    = {2023},
#}

#Imput handler
try:
 if sys.argv[1] is not None:
  if sys.argv[1] == "firstrun":
   x = -1
  else:
   x = int(sys.argv[1])
   if x < 1:
    x = x * -1
except:
  x = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
if x == 0:
 exit('0 will not be prime');

#Functions
def fileread(primes):
 primefile = open("_data", "r")
 primes = primefile.read().split(",")
 primefile.close
 return primes

def filesave(data):
 content = str(data)
 primefile = open("_data", "w")
 primefile.write(content)
 primefile.close

def findprime(x, i):
 if instance(x / i, int):
  return(true)
 else:
  return(false)

#Development proof
primes = 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71

filesave(primes)
primes = ""
primes = fileread(primes)

print (x)
print (primes)
print (primes[11])
print (int(primes[11]))

#Runtime
if x == -1: #firstrun
 arp = 1
 while len(primes) <= 10000:
  i = primes


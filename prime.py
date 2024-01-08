#!/usr/bin/python
## Prime
# Takes an input and return all primes up to input
# prime.py script
# Source Code produced by Willtech 2023
# v0.1 hand coded by HRjJ

#prime.py [number to check] []

print("Initialise...")
## setup dependencies
import sys
import re

from mpmath import *
mp.dps = 5000000000 
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
   mp.dps = len(str(int(sys.argv[1])))
   x = mpf(sys.argv[1])
   if x < 1:
    x = x * -1
except:
  mp.dps = 185
  x = mpf('531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127')
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
 mp.dps = len(str(x))
 #print (str(mpf(x)), str(mpf(i))) #
 #print (str(mpf(x) / i)) #
 #print (str(mpf(x) / i).split(".")[1]) #
 if str(mpf(x) / i).split(".")[1] == "0":
  print (i, 'Doh!') #
  return(False)
 else:
  print (i, 'Ding!') #
  return(True)

def createint(i):
 return(int(i))

#Development proof
primes = 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71

filesave(primes)
primes = ""
primes = fileread(primes)

#print (x) #
#print (primes) #
#print (len(primes)) #
#print (primes[11]) #
#print (createint(primes[11])) #
#print (len(str(x))) #

#Runtime
if x == -1: #firstrun
 print ("Firstrun: Building _data")
 arp = 1
 primes = ""
 primes = 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71
 while len(primes) <= 1000:
  mp.dps = mpf(str(primes[len(primes)-1]))
  x = mpf(str(primes[len(primes)-1]+2))
  if findprime(x, 2):
   i = primes[arp]
   while i < x / i:
    if findprime(x, i):
     arp = arp + 1
     i = primes[arp]
    else:
     arp = 1
     i = primes[arp]
     x = x + 2
   print ("Found", x)
   arp = 1
   primes = (*primes, int(x))
  else:
   print (primes)
   print ('Looking for', x)
   exit ('Math error creating _data.');

filesave(primes)
fileread(primes)
# print(primes) #
print ('Completed creating data to', len(primes)-1, 'Primes');
exit ('Largest Prime in Index:' + str(primes[len(primes)-1]))

#sample
mp.dps = len(str(primes[len(primes)-1]))
x = mpf('169')
i = 13
print(str(mpf(x) / i))

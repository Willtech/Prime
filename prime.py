#!/usr/bin/python
## Prime
# Takes an input and return all primes up to input
# prime.py script
# Source Code produced by Willtech 2023
# v0.1 hand coded by HRjJ

#prime.py [number to check] []
import time
tt = time.time()

print("Initialise...")
## setup dependencies
import sys
import re

from mpmath import *
mp.dps = 15000000000
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
   try:
    mp.dps = len(str(int(sys.argv[1])))
    x = mpf(str(sys.argv[1]))
   except:
    exit ("Input error.")
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
 j = mpf(x) / i
 if str(j).split(".")[1] == "0":
#  printoutput (x, i, j, 'Doh!') #
  return (False)
 else:
#  printoutput (x, i, j, 'Ding!') #
  return (True)

def printoutput(x, i, j, f):
 print ('Dividend:', x)
 print ('Divisor:', i)
 print ('Quotient:', j, 'from divisor:', i, f)
 print ('---')

def printfound(x):
 print ('Found:', x)
 print ('------')

def createint(i):
 return(int(i))

#Development proof
#primes = ""
#primes = fileread(primes)

#Runtime
if x == -1: #firstrun
 print ("Firstrun: Building _data")
 arp = 1
 primes = ""
 primes = 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71
 mp.dps = mpf(len(str(primes[len(primes)-1])))
 while len(primes) <= 1000000:
  arp = 1
  x = mpf(str(primes[len(primes)-1]+2))
  mp.dps = len(str(x))
  if findprime(x, 2):
   i = createint(primes[arp])
   while i < x / i:
    i = createint(primes[arp])
    if findprime(mpf(x), i):
     arp = arp + 1
    else:
     arp = 1
     x = x + 2
   printfound(x) #
   primes = (*primes, int(x))
  else:
   print (primes)
   print ('Looking for', x)
   exit ('Math error creating _data.');

 filesave(primes)
 fileread(primes)
 # print(primes) #
 print ('Completed creating data to', len(primes)-1, 'Primes');
 print ('Largest Prime in Index:' + str(int(''.join(filter(str.isdigit, str(primes[len(primes)-1]))))))
 exit ("--- %s Seconds ---" % (time.time() - tt))

#Main

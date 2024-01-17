#!/usr/bin/python
## Prime
# Takes an input and return all primes up to input
# prime.py script
# Source Code produced by Willtech 2023
# v0.3 hand coded by HRjJ
import time
tt = time.time()

#prime.py [number to check] []

# print("Initialise...") #
## setup dependencies
import sys
import re
import os

from mpmath import *
mp.dps = 15000000000
subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#@manual{mpmath,
#  key     = {mpmath},
#  author  = {The mpmath development team},
#  title   = {mpmath: a {P}ython library for arbitrary-precision floating-point arithmetic (version 1.3.0)},
#  note    = {{\tt http://mpmath.org/}},
#  year    = {2023},
#}

#Imput handler
if len(sys.argv) > 1:
 if (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
  print ('Usage: prime.py [OPTIONS | N]')
  print ('    Searches using Vignette Sieve up to N for Prime and on completion')
  print ('    incorporates each new Prime found in _data.')
  print ('')
  print ('Options:')
  print ('  General Options:')
  print ('    -h, --help                           Print this help and exit')
  print ('    firstrun [M]                         Operates in firstrun mode to generate')
  print ('                                         _data file up to 1,000,000th Prime or')
  print ('                                         when M is specified counts up to a Prime')
  print ('                                         of that magnitude.')
  sys.exit(0)
 try:
  if sys.argv[1] == "firstrun":
   x = -1
  else:
   try:
    mp.dps = str(len(str(int(sys.argv[1]))))
    x = mpf(str(sys.argv[1]))
   finally:
    if x < 1:
     x = x * -1
 except:
  exechelp = ('py ' + os.path.realpath(__file__) + ' -h')
  os.system(exechelp)
  sys.exit(1)
else:
 exechelp = ('py ' + os.path.realpath(__file__) + ' -h')
 os.system(exechelp)
 sys.exit(1)

if  len(sys.argv) > 2:
 try:
  m = mpf(str(sys.argv[2]))
 except:
  exechelp = ('py ' + os.path.realpath(__file__) + ' -h')
  os.system(exechelp)
  sys.exit(1)
else:
 m = 1000

if x == 0:
 exit('0 will not be prime.');

if x == 1:
 exit('1 is self Prime.');

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
 j = mpf(x) / createint(i)
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

def printfound(x, p):
 print ('Found: P',str(p).translate(subscript), ' is ', str(x).split(".")[0], sep='')
 print ('------')

def createint(i):
 return(int(i))

#Development proof
# primes = ""
# primes = fileread(primes)

#Runtime
#Firstrun
if x == -1: #firstrun
 print ("Firstrun: Building _data")
 arp = 1
 primes = ""
 primes = 1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71
 mp.dps = mpf(str(len(str(primes[len(primes)-1]))))
 while len(primes) <= m:
  arp = 1
  y = str(primes[len(primes)-1])
  y = int(''.join(filter(str.isdigit, y)))
  x = mpf(str(createint(y+2)))
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
   printfound(x, len(primes)) #
   primes = (*primes, int(x))
  else:
   print (primes)
   print ('Looking for', x)
   exit ('Math error creating _data.');

# filesave(primes)
 fileread(primes)
#   print(primes) #
 print ('Completed creating data to', len(primes)-1, 'Primes');
 print ('Largest Prime in Index:' + str(int(''.join(filter(str.isdigit, str(primes[len(primes)-1]))))))
 exit ("--- %s Seconds ---" % (time.time() - tt))

#Main
print ('Checking', str(x).split(".")[0], 'for Prime:') 
exit('Not yet implement.')

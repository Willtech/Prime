#!/usr/bin/python
from mpmath import *
mp.dps = 10000
#@manual{mpmath,
#  key     = {mpmath},
#  author  = {The mpmath development team},
#  title   = {mpmath: a {P}ython library for arbitrary-precision floating-point arithmetic (version 1.3.0)},
#  note    = {{\tt http://mpmath.org/}},
#  year    = {2023},
#}

l = 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
print ('l =', l)
n = 9
print ('n =', n)
print ('l / n =', l/n)
print ('mpf(l) / n =', mpf(l)/n)

print ()
n = 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
print ('l =', l)
print ('n =', n)
print ('l / n =', l/n)
print ('mpf(l) / n =', mpf(l)/n)

print (mpf(123348809755013372855351771562296686142137618828897016962516049052308667842740497131311830445)/39263145594024355220320754655847602065090387900339386891430760274478663119563892301334897957)

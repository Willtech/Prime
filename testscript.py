#!/usr/bin/python
## testscript
# pruns some inputs on prime.py
# testscript.py script
# Source Code produced by Willtech 2023
# v0.1 hand coded by HRjJ
import os

print ('py prime.py firstrun')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' firstrun')
os.system(exechelp)

print ('---------')

print ('py prime.py --help')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' --help')
os.system(exechelp)

print ('---------')

print ('py prime.py -h')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' -h')
os.system(exechelp)

print ('---------')

print ('py prime.py 0')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' 0')
os.system(exechelp)

print ('---------')

print ('py prime.py 1')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' 1')
os.system(exechelp)

print ('---------')

print ('py prime.py 123')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' 123')
os.system(exechelp)

print ('---------')

print ('py prime.py -123')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' -123')
os.system(exechelp)

print ('---------')

print ('py prime.py 7')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' 7')
os.system(exechelp)

print ('---------')

print ('py prime.py -7')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' -7')
os.system(exechelp)

print ('---------')

print ('py prime.py ab12')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' ab12')
os.system(exechelp)

print ('---------')

print ('py prime.py 12ab')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' 12ab')
os.system(exechelp)

print ('---------')

print ('py prime.py abc')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py' + ' abc')
os.system(exechelp)

print ('---------')

print ('py prime.py')
exechelp = ('py ' + os.path.abspath(os.path.dirname(__file__)) + '/prime.py')
os.system(exechelp)



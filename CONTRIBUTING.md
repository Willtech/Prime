# Contributing to Prime
You might be interested the search for Prime is long found. Any number divisible only by one and itself is Prime and one is self-Prime. Optimising the search for Prime continues. There is an opportunity for contributors on a research project I have started on GitHub:Willtech/Prime believing my initial work is good enough to be empirical as far as I have tested, I have noted some further optimisations I intend to test. Not the same as a wheel function instead using the traditional Dividend Divisor Quotient method a "Vignette Seive" optimisation and only tries numbers that could possibly be Prime, and can be further developed to make the least checking possible using the elimination from trial of numbers that cannot possibly be Prime from information gained from a sieve of Eratosthenes. Interested contributors are welcome.

## Getting Started

New contributors ase most welcome. 

Testing and researching code is a fickle affair. There are hundreds of ways to solve most problems compuationally.

Before contirbuting, take time to familiaraise yourself with the research and the operation of the program. You should reaslise the program even the Mathematics works with strings using mpmath (The mpmath development team., 2023).

## Contributing

Contributions that are 'smarter' that do not optimise will not be considered.

First create an Issue to discuss the optimisation.

`git clone` the project and then test the changes you propose. The output must be valdated to at lease one-million Prime in your commit.

Create a one-line attrubution comment beneath the opening block of the program with your name and comment to reference your contribution and include any references required including inline block comments with the code you submit. Let us worry about version increments e.g.

```Python
#!/usr/bin/python
## Prime
# Takes an input and return all primes up to input
# prime.py script
# Source Code produced by Willtech 2023
# v0.4 hand coded by HRjJ
# Contributor, D. (2024) Optimise program handling of faster array
import time
tt = time.time()

#prime.py [number to check] []
firstrun = 1000000 # Amount of firstrun n for Pn to create in _data

...


# Ref <<<
## The mpmath development team. (2023). mpmath - Python library for arbitrary-precision floating-point arithmetic. Retrieved February 2, 2024, from https://mpmath.org/
```


Squash your commit before creating a Pull Request.

All Pull Requests should link to the discussion in their issue.

Be descriptive with your comments, how you solve some problem and what it accomplishes.

It can take some time before there is an opportunity to test proposed contributions.

## Appendix

### Reference

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">The mpmath development team. (2023). mpmath - Python library for arbitrary-precision floating-point arithmetic. Retrieved February 2, 2024, from https://mpmath.org/</p>

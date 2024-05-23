# Prime
## An attempt to optimise the search for prime.

### Abstract
A Prime is any number only divisible by 1 and itself searching first that a number is not even if it divides by 2, optimising using a "Vignette Sieve" that if not only up to n/2 needs to be tested as a divisor, then 3 if not only up to n/3 needs to be tested as divisor, n/5, n/7, n/11, n/13, n/17, n/19, n/23, n/29, n/31 & so on so that only divisibility by a prime needs to be checked for to prove not prime & since for example we have ruled out that the number is a factor of three or two so there is no natural number greater than n/3 that can be a divisor.

### Usage
On first run use `prime.py firstrun` to build the data table. The data table *may be* provided. It can find up to 104729 the 10,000th Prime in under 6 seconds and can possibly be accellerated with `mpiexec`

```log prime.py firstrun
$py prime.py firstrun
Firstrun: Building _data
Completed creating data to 10000 Primes
Largest Prime in Index:104729
--- 5.355212926864624 Seconds ---
```

#### Future implementation in development

`prime.py [number to check]`

Output: List of Prime numbers up to the input. If only the output prime or not prime is required edit `prime.py`.

File `_data` contains the raw found prime data.

### Operation
`prime.py` will use the data table of found prime numbers to optimise the search for prime up to the Vignette Sieve fraction necessary & when searching above found primes will search for additional prime numbers & add these to the data to test the input for prime. This approach is optimised heavily because it is only necessary to check up to the highest fraction divisor of the number already checked n/x. The Vignette Seive is a convergance function I have written as the Integral described in Image1  
[![The Integral of is x Prime](./Images/The%20Integral%20-%20Is%20Prime.png "Links to WolframAlpha")][3]  
*Image1: The Integral of is x Prime. Professor. Damian A. James Williamson  
Links to: WolframAlpha*

Prime numbers are defined as numbers greater than 1 that have no positive divisors other than 1 and themselves. 1 is self-Prime. The sequence of prime numbers starts with 2, 3, 5, 7, 11, and so on.
 
It should be possible to run with `mpiexec` [Build a Raspberry Pi cluster computer][1]

Professor. Damian A. James Williamson

=======
## Appendix

### Future Optimisations

Notes: [LinkedIn comments][4]

Optimising further than checking only if a number is not even it is possible to check only if a number is one more or less than a factor of 6 so counting for 5 is +2 for 7 and +4 for 11 and so forth. Then when counting from a high number counting back to a number divisible by 6 if it is 1 less add 4 to the number we started with and if it is 5 less add 2 then continue as previously.

It should be possible to have in addition to a find next Prime function a find next number to check from unknown sequence and find next number from known position in sequence. The approach is to build the functions necessary into firstrun that searches by magnitude providing a proof and then build main that validates an individual number. The easiest wat to check whether to check a number is to check if it is dividible by 6 and then if it is one number more or less than 6, say if we look at 11 it is  not divisible by 6 and it is one less than 6 so we try. This saves a lot of computation with larger numbers. 

Professor. Damian A. James Williamson

### Reference

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">The mpmath development team. (2023). mpmath - Python library for arbitrary-precision floating-point arithmetic. Retrieved February 2, 2024, from https://mpmath.org/</p>

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">Mathematics Stack Exchange. (2013). multiplicative function - How to find the nearest multiple of 16 to my given number n - Mathematics Stack Exchange. Retrieved February 2, 2024, from https://math.stackexchange.com/questions/291468/how-to-find-the-nearest-multiple-of-16-to-my-given-number-n</p>

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">Stack Overflow. (2010). How to extract numbers from a string in Python? - Stack Overflow. Retrieved February 2, 2024, from https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python</p>

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">Stack Overflow. (2010). python - Checking whether a variable is an integer or not - Stack Overflow. Retrieved February 2, 2024, from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not</p

<p class="apa-reference" style="padding-left: 36px; text-indent: -36px;">Phillips, C. (2015). Writing Mathematics in Plain Text Email. Retrieved January 24, 2024, from https://pages.uoregon.edu/ncp/Courses/MathInPlainTextEmail.html</p>

[1]: https://magpi.raspberrypi.com/articles/build-a-raspberry-pi-cluster-computer
[2]: ./Images/The%20Integral%20-%20Is%20Prime.png
[3]: https://www.wolframalpha.com/input?i2d=true&i=x+is+natural+number+if+PrimeIntegrate%5B%5C%2840%29n+%3C+Divide%5Bx%2Cn%5D%5C%2841%29%2C%7B%5C%2840%29x+%25+P%E2%82%99+%E2%89%A0+0%5C%2841%29%2CP%E2%82%99%2CP%E2%82%81%7D%5D%3D%E2%8A%A4%E2%88%B4+x+is+Prime
[4]: https://www.linkedin.com/feed/update/urn:li:activity:7152930677804421120?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7152930677804421120%2C7155347903270522880%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287155347903270522880%2Curn%3Ali%3Aactivity%3A7152930677804421120%29

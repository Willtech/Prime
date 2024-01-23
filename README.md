# Prime
## An attempt to optimise the search for prime.

### Abstract
A Prime is any number only divisible by 1 and itself searching first that a number is not even if it divides by 2, optimising using a "Vignette Sieve" that if not only up to n/2 needs to be tested as a divisor, then 3 if not only up to n/3 needs to be tested as divisor, n/5, n/7, n/11, n/13, n/17, n/19, n/23, n/29, n/31 & so on so that only divisibility by a prime needs to be checked for to prove not prime & since for example we have ruled out that the number is a factor of three or two so there is no natural number greater than n/3 that can be a divisor.

### Usage
On first run use `prime.py firstrun` to build the data table. The data table *may be* provided. It can find up to 104729 the 10,000th Prime in 6 seconds and can be faster with `mpiexec`

```log prime.py firstrun
Initialise...
Firstrun: Building _data
Completed creating data to 10000 Primes
Largest Prime in Index:104729
```

`prime.py [number to check]`

Output: List of Prime numbers up to the input. If only the output prime or not prime is required edit `prime.py`.

File `_data` contains the raw found prime data.

### Operation
`prime.py` will use the data table of found prime numbers to optimise the search for prime up to the Vignette Sieve fraction necessary & when searching above found primes will search for additional prime numbers & add these to the data to test the input for prime. This approach is optimised heavily because it is only necessary to check up to the highest fraction divisor of the number already checked n/x. It is a convergance function.

It should be possible to run with `mpiexec` [Build a Raspberry Pi cluster computer][1]

### Future Optimisations

Notes: [LinkedIn comments][2]

Optimising further than checking only if a number is not even it is possible to check only if a number is one more or less than a factor of 6 so counting for 5 is +2 for 7 and +4 for 11 and so forth. Then when counting from a high number counting back to a number divisible by 6 if it is 1 less add 4 to the number we started with and if it is 5 less add 2 then continue as previously.

It should be possible to have in addition to a find next Prime function a find next number to check from unknown sequence and find next number from known position in sequence. The approach is to build the functions necessary into firstrun that searches by magnitude providing a prrof and then build main that validates an individual number. The easiest wat to check whether to check a number is to check if it is dividible by 6 and then if it is one number more or less than 6, say if we look at 11 it is  not divisible by 6 and it is one less than 6 so we try. This saves a lot of computation with larger numbers. 

Professor. Damian A. James Williamson

[1]: https://magpi.raspberrypi.com/articles/build-a-raspberry-pi-cluster-computer
[2]: https://www.linkedin.com/feed/update/urn:li:activity:7152930677804421120?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7152930677804421120%2C7155347903270522880%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287155347903270522880%2Curn%3Ali%3Aactivity%3A7152930677804421120%29

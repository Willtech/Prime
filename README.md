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

Professor. Damian A. James Williamson

[1]: https://magpi.raspberrypi.com/articles/build-a-raspberry-pi-cluster-computer


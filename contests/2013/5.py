#!/usr/bin/env python

"""
not my solution

I feel like this solution has something to do with Euclid's algorithm for
finding the GCD
"""

with open("s5.in", 'r') as infile:
    number = int(infile.readline().strip())

cost = 0


def find_smallest_factor(number):
    #largest number we need to go to before concluding number is prime
    max_factor = int(number ** 0.5) + 1
    if number % 2 == 0:
        return 2
    for factor in range(3, max_factor, 2):
        if number % factor == 0:
            return factor


while number != 1:  # 1 is what we're trying to get to
    factor = find_smallest_factor(number)
    if factor:
        #everything that is left after the smallest factor is divided out
        leftover = number / factor
        #number can be reduced by this because
        number -= leftover
        cost += number / leftover
    else:  # if number is prime, go back only 1
        number -= 1
        cost += number


print cost
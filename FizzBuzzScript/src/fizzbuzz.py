'''
Created on 18-08-2012

@author: kfigaj
'''
from sys import argv


def fizzbuzz(number):
    """
    Fizz buzz is a counting game where each player speaks a number from 1 to n
    in sequence, but with a few exceptions:
    - if the would-be spoken number is divisible by 3 the player must say fizz
    instead
    - if the would-be spoken number is divisible by 5 the player must say buzz
    instead
    - if the would-be spoken number is divisible by 3 and 5 the player must say
    fizzbuzz instead
    """
    output = []
    for i in range(1, int(number) + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                value = 'fizzbuzz'
                output.append
            else:
                value = 'fizz'
        elif i % 5 == 0:
            value = 'buzz'
        else:
            value = i
        print value
        output.append(value)
    return output


if __name__ == '__main__':
    try:
        script, first = argv
        fizzbuzz(first)
    except (ValueError, TypeError) as e:
        print """This is a simple FizzBuzz application. 
Please provide a number of rounds as a first parameter of script.
First argument must be a positive integer.
No other arguments are accepted.
Example: $ python fizzbuzz.py 10!"""

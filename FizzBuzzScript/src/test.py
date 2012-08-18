'''
Created on 18-08-2012

@author: kfigaj
'''
import unittest
import subprocess


class FizzBuzzTest(unittest.TestCase):

    # Expected output for fizzbuzz 15
    FIZZBUZZ15 = """1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
"""

    ERROR_OUTPUT = """This is a simple FizzBuzz application.
Please provide a number of rounds as a first parameter of script.
First argument must be a positive integer.
No other arguments are accepted.
Example: $ python fizzbuzz.py 10!
"""

    def testFizzBuzz(self):
        output = subprocess.check_output(["python fizzbuzz.py 15"],
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEquals(self.FIZZBUZZ15, output,
            "Output value {} doesnot match expected value {}!"
            .format(output, self.FIZZBUZZ15)
        )

    def testTooFewArguments(self):
        output = subprocess.check_output("python fizzbuzz.py",
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEquals(self.ERROR_OUTPUT, output,
            "Output value {} doesnot match expected value {}!"
            .format(output, self.ERROR_OUTPUT)
        )

    def testTooManyArguments(self):
        output = subprocess.check_output(["python fizzbuzz.py 15 jack sparrow"],
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEquals(self.ERROR_OUTPUT, output,
            "Output value {} doesnot match expected value {}!"
            .format(output, self.ERROR_OUTPUT)
        )

    def testFirstArgumentIsNotInteger(self):
        output = subprocess.check_output(["python fizzbuzz.py five"],
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEquals(self.ERROR_OUTPUT, output,
            "Output value {} doesnot match expected value {}!"
            .format(output, self.ERROR_OUTPUT)
        )

    def testFirstArgumentIsNotPositiveInteger(self):
        output = subprocess.check_output(["python fizzbuzz.py -5"],
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEquals(self.ERROR_OUTPUT, output,
            "Output value {} doesnot match expected value {}!"
            .format(output, self.ERROR_OUTPUT)
        )

if __name__ == "__main__":
    unittest.main()

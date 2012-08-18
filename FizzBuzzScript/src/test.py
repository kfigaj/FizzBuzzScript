'''
Created on 18-08-2012

@author: kfigaj
'''
import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    # Expected output for fizzbuzz 15
    FIZZBUZZ15 = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', \
              11, 'fizz', 13, 14, 'fizzbuzz']

    def testFizzBuzz(self):
        value = fizzbuzz(15)
        self.assertEquals(self.FIZZBUZZ15, value,
            "Output value {} doesnot match expected value {}!"
            .format(value, self.FIZZBUZZ15)
        )

if __name__ == "__main__":
    unittest.main()

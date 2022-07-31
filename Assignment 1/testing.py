from audioop import add
from functionsToTest import exponent, multiplication, addition, subtraction, squareRoot
import unittest


class exponentUnitTest(unittest.TestCase):
    def testOne(self):
        assert exponent(2, 3) == 8, "Cannot take exponent of positive numbers"

    def testTwo(self):
        assert exponent(-2, -3) ==  -0.125, "Can't have negative exponent of a negative value"

    def testThree(self):
        assert exponent(-2, 3) ==  -8, "Can't take exponent of a negative number"


class multiplicationUnitTest(unittest.TestCase):
    def testOne(self):
            assert multiplication(1, 2) == 2, "Can't multiply positive numbers"

    def testTwo(self):
            assert multiplication(-2, -3) == 6, "Can't multiply negative numbers"

    def testThree(self):
            assert multiplication(-4, 5) == -20, "Can't multiply positive and negative numbers"


class additionUnitTest(unittest.TestCase):
    def testOne(self):
            assert addition(1, 2) == 3, "Can't add positive numbers"

    def testTwo(self):
            assert addition(-2, -3) == -5, "Can't add negative numbers"

    def testThree(self):
            assert addition(-4, 5) == 1, "Can't add negative and positive numbers"


class subtractionUnitTest(unittest.TestCase):
    def testOne(self):
            assert subtraction(1, 2) == -1, "Can't subtract positive numbers"

    def testTwo(self):
            assert subtraction(-3, -4) == 1, "Can't subtract negative numbers"

    def testThree(self):
            assert subtraction(-5, 6) == -11, "Can't subtract positive and negative numbers"


class squareRootUnitTest(unittest.TestCase):
    def testOne(self):
            assert squareRoot(4) == 2.0, "Can't find square root of a positive number"

    def testTwo(self):
            assert squareRoot(-8) == (1.7319121124709868e-16+2.8284271247461903j), "Can't find square root of a negative number"

    def testThree(self):
            assert squareRoot(0) == 0.0, "Can't find square root of zero"



def exponentSuite():
        suite = unittest.TestSuite()
        suite.addTest(exponentUnitTest('testOne'))
        suite.addTest(exponentUnitTest('testTwo'))
        suite.addTest(exponentUnitTest('testThree'))
        return suite

def multiplicationSuite():
        suite = unittest.TestSuite()
        suite.addTest(multiplicationUnitTest('testOne'))
        suite.addTest(multiplicationUnitTest('testTwo'))
        suite.addTest(multiplicationUnitTest('testThree'))
        return suite

def additionSuite():
        suite = unittest.TestSuite()
        suite.addTest(additionUnitTest('testOne'))
        suite.addTest(additionUnitTest('testTwo'))
        suite.addTest(additionUnitTest('testThree'))
        return suite

def subtractionSuite():
        suite = unittest.TestSuite()
        suite.addTest(subtractionUnitTest('testOne'))
        suite.addTest(subtractionUnitTest('testTwo'))
        suite.addTest(subtractionUnitTest('testThree'))
        return suite

def squareRootSuite():
        suite = unittest.TestSuite()
        suite.addTest(squareRootUnitTest('testOne'))
        suite.addTest(squareRootUnitTest('testTwo'))
        suite.addTest(squareRootUnitTest('testThree'))
        return suite


def main():
    while True:
        inputOne = int(input("What unit test do you want to run?\n1) Exponent\n2) Multiplication\n"
        "3) Addition\n4) Subtraction\n5) Square Root\n6) None\n"))

        if inputOne == 1:
            suiteToTest = exponentSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 2:
            suiteToTest = multiplicationSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 3:
            suiteToTest = additionSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 4:
            suiteToTest = subtractionSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 5:
            suiteToTest = squareRootSuite()
            unittest.TextTestRunner(verbosity = 2).run(suiteToTest)

        if inputOne == 6:
            print("\nPROGRAM TERMINATED\n")
            break
        
main()



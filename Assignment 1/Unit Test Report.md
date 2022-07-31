# Test Report

## Assignment Goal
The primary objective of the assignment given to us was unit testing of five functions of our choice.

## Functions I am testing
| Function      | Purpose |
| ----------- | ----------- |
| ``exponent``    | Takes arguments a and b, returns b as an exponent of a      |
| ``multiplication``  | Takes arguments a and b, returns their product     |
| ``addition``     | Takes arguments a and b, returns their sum      |
| ``subtraction``  | Takes arguments a and b, subtracts b from a and returns the value       |
| ``squareRoot``    | Takes a single argument a, returns its square root     |

All these functions can be seen in the `functionsToTest.py` file. <br>
All the work here is done in Python.

## Logic behind the edge cases

### ``exponent``
Here I am testing 6 edge cases:
1. Positive base and positive exponent.
2. Negative base and negative exponent.
3. Negative base and positive exponent.
4. 0 base and positive exponent.
5. Positive base and 0 exponent.
6. Positve base and negative exponent.

### ``multiplication``
Multiplication follows commutative law, so the edge cases will not have to be repeated for the same values in different positions. I am testing four edge cases here:
1. Multiplication between two positive numbers.
2. Multiplication between two negative numbers.
3. Multiplication between a positive and a negative number.
4. Multiplication with 0.

### ``addition``
Addition also follows the commutative law. I am testing four edge cases for ```addition```:
1. Addition between two positive numbers.
2. Addition between two negative numbers.
3. Addition between a negative and a positive number.
4. Addition to a 0.

### ``subtraction``
Subtraction does not follow the commutative law, so it was necessary to test more cases. I tested six edge cases for subtraction.
1. Subtraction of a positive number from a positive number.
2. Subtraction of a negative number from a negative number.
3. Subtraction of a positive number from a negative number.
4. Subtraction of a negative number from a positive number.
5. Subtraction of a number from 0.
6. Subtraction of 0 from a number.

## ``squareRoot``
I tested three edge cases for this function:
1. Square root of a positive number.
2. Square root of a negative number.
3. Square root of 0.


# Test Report

## Assignment Goal
The primary objective of the assignment given to us was unit testing of five functions of our choice.

## Functions I am testing
| Function      | Purpose |
| ----------- | ----------- |
| ``exponent``    |<img width="168" alt="Screenshot 2022-07-31 at 10 07 28 PM" src="https://user-images.githubusercontent.com/64619851/182037604-a08b1e6b-60d0-4f67-951a-909793184672.png"> <br> Takes arguments a and b, returns b as an exponent of a|
| ``multiplication``  |<img width="215" alt="Screenshot 2022-07-31 at 10 07 31 PM" src="https://user-images.githubusercontent.com/64619851/182037640-442b9c52-b917-495e-a578-34bc46109659.png"> <br> Takes arguments a and b, returns their product     |
| ``addition``     | <img width="185" alt="Screenshot 2022-07-31 at 10 07 33 PM" src="https://user-images.githubusercontent.com/64619851/182037649-ce767a78-2f5a-4309-ae44-fa4235b6ab2f.png"> <br> Takes arguments a and b, returns their sum      |
| ``subtraction``  | <img width="199" alt="Screenshot 2022-07-31 at 10 07 36 PM" src="https://user-images.githubusercontent.com/64619851/182037655-f7bcf882-c48b-4dfe-a9cd-fdef74cd6861.png"> <br> Takes arguments a and b, subtracts b from a and returns the value       |
| ``squareRoot``    |<img width="214" alt="Screenshot 2022-07-31 at 10 07 39 PM" src="https://user-images.githubusercontent.com/64619851/182037659-1bd87510-6db1-472a-a717-4cb900104dd2.png"> <br> Takes a single argument a, returns its square root     |

All these functions can be seen in the `functionsToTest.py` file. <br>
All the work here is done in Python.

## Logic behind the edge cases

## ``exponent``
Here I am testing 6 edge cases:
1. Positive base and positive exponent.
2. Negative base and negative exponent.
3. Negative base and positive exponent.
4. 0 base and positive exponent.
5. Positive base and 0 exponent.
6. Positve base and negative exponent.
<img width="870" alt="Screenshot 2022-07-31 at 10 06 21 PM" src="https://user-images.githubusercontent.com/64619851/182037718-68144c25-1c26-47bb-a757-c4771fd420a1.png">


## ``multiplication``
Multiplication follows commutative law, so the edge cases will not have to be repeated for the same values in different positions. I am testing four edge cases here:
1. Multiplication between two positive numbers.
2. Multiplication between two negative numbers.
3. Multiplication between a negative and a positive number.
4. Multiplication with 0.
<img width="811" alt="Screenshot 2022-07-31 at 10 06 30 PM" src="https://user-images.githubusercontent.com/64619851/182037746-0a25fac5-5211-4edd-ab10-d21f65dea6c2.png">



## ``addition``
Addition also follows the commutative law. I am testing four edge cases for ```addition```:
1. Addition between two positive numbers.
2. Addition between two negative numbers.
3. Addition between a negative and a positive number.
4. Addition to a 0.
<img width="721" alt="Screenshot 2022-07-31 at 10 06 34 PM" src="https://user-images.githubusercontent.com/64619851/182037732-307ae7dc-8032-486c-a4e6-952bb7f6697b.png">


## ``subtraction``
Subtraction does not follow the commutative law, so it was necessary to test more cases. I tested six edge cases for subtraction.
1. Subtraction of a positive number from a positive number.
2. Subtraction of a negative number from a negative number.
3. Subtraction of a positive number from a negative number.
4. Subtraction of a negative number from a positive number.
5. Subtraction of a number from 0.
6. Subtraction of 0 from a number.
<img width="820" alt="Screenshot 2022-07-31 at 10 06 41 PM" src="https://user-images.githubusercontent.com/64619851/182037729-3ddeb24a-670b-4e36-894c-f3ec46767224.png">


## ``squareRoot``
I tested three edge cases for this function:
1. Square root of a positive number.
2. Square root of a negative number.
3. Square root of 0.
<img width="1039" alt="Screenshot 2022-07-31 at 10 07 14 PM" src="https://user-images.githubusercontent.com/64619851/182037727-85ab42a8-6601-4510-b532-b197f944d4a5.png">


## Errors found
## ``exponent``
<img width="345" alt="Screenshot 2022-07-31 at 9 52 16 PM" src="https://user-images.githubusercontent.com/64619851/182037029-55602cf7-d1e6-49a9-a39c-41e86173ce5b.png">
No errors found in this function.

## ``multiplication``
<img width="390" alt="Screenshot 2022-07-31 at 9 52 23 PM" src="https://user-images.githubusercontent.com/64619851/182037030-9490bd83-139c-44cd-aea4-31bbddc6aa1a.png">
No errors found in this function.

## ``addition``
<img width="343" alt="Screenshot 2022-07-31 at 9 52 31 PM" src="https://user-images.githubusercontent.com/64619851/182037034-8fe1d4d9-3a5d-476e-86d7-7b6857b95c94.png">
No errors found in this function.

## ``subtraction``
<img width="361" alt="Screenshot 2022-07-31 at 9 52 41 PM" src="https://user-images.githubusercontent.com/64619851/182037039-c099e8eb-124e-4bca-a298-cb3d4abaac87.png">
No errors found in this function.

## ``squareRoot``
<img width="373" alt="Screenshot 2022-07-31 at 9 52 48 PM" src="https://user-images.githubusercontent.com/64619851/182037043-2a9d17e0-f30b-4811-9f28-6de41a750744.png">
No errors found in this function.

#### Total tests: 23
#### Tests passed: 23
#### Tests failed: 0
#### Success rate: 100%
#### Failure rate: 0%

## Programs Used
You simple write ``import unittest`` to import the [PyUnit](http://pyunit.sourceforge.net/pyunit.html) module for unit testing in Python. No specific softwares, IDEs or text-editors are required.

# Assignment 2a: Significant figures

Write program code to:

1. Ask the user to input a number (decimal or integer)
2. Determine the number of significant figures in the number
3. Print the number of significant figures (sf).

You should **process** the input by stripping any whitespace around the numbers.

The following set of rules are used to determine if a digit is significant:

- All non-zero digits are significant: 1, 2, 3, 4, 5, 6, 7, 8, 9.
- Zeros between non-zero digits are significant: 102, 2005, 50009.
- Leading zeros are never significant: 0.02, 001.887, 0.000515.
- In a number with or without a decimal point, trailing zeros (those to the right of the last non-zero digit) are significant provided they are justified by the precision of their derivation: 389000; 2.02000; 5.400; 57.5400.  
- For the purpose of this assignment, you may assume that all trailing zeros are justified by the precision of their derivation.

### Example

    Enter a number (decimal or integer): 2.345
    The number 2.345 has 4 significant figures.
          
    Enter a number (decimal or integer): 02.345
    The number 02.345 has 4 significant figures.
          
    Enter a number (decimal or integer): 0.0023
    The number 0.0023 has 2 significant figures.
          
    Enter a number (decimal or integer): 2.3400
    The number 2.3400 has 5 significant figures.

# Submission

Before submitting, run the tests on your final code.

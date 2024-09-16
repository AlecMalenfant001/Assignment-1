# Intro to AI Assignment-1 Problem-1

# By Alec Malenfant

## Overview

This program will find the absolute difference between the diagonals of a square matrix

For example, the square matrix is shown below:
<br/>1 2 3
<br/>4 5 6
<br/>9 8 9

The left-to-right diagonal 1 + 5 + 9 = 15 . The right to left diagonal 3 + 5 + 9 = 17.
Their absolute difference is |15 – 7| = 2.

## Input

This program is user input driven. There are some checks on the inputs to ensure that positive integers are within accepted domain, but if non-integer data is entered then the program will crash.

### Matrix Dimensions

First, the user must enter a positive integer to define the size of the matrix. For every input n the program will create a n x n matrix. The size limit for a matrix is 99 x 99

### Matrix Data Entry

Next the user will enter the matrix data row-wise. The user should enter each row as a line of integers separated by a space.

For example, this is how a 3x3 matrix would be entered:
<br/> 1 2 3
<br/> 4 5 6
<br/> 7 8 9

These integers can be positive or negative

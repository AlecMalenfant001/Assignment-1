# Alec Malenfant amalenf@pnw.edu
# Assignment 1
# Problem 1
import numpy as np


# Get Input from user
# Instructions in a readme.txt file
# For now we will use a fixed 3x3 matrix
a = np.array([[1, 2, 3], [4, 5, 6], [9, 8, 9]])


# Get sum of left-to-right diagonal
def sumLeftToRightDiagonal():
    leftToRightDiagonal = np.diagonal(a) # get the left-to-right diagonal
    return np.sum(leftToRightDiagonal) # return the sum of the diagonal

# Get Sum of right-to-left diagonal
def sumRightToLeftDiagonal():
    rightToLeftDiagonal = np.fliplr(a).diagonal() # get the right-to-left diagonal
    return np.sum(rightToLeftDiagonal) # return the sum of the diagonal

# Get absolute difference of diagonals
def printAbsoluteDifference():
    print("|" + str(sumLeftToRightDiagonal()) + " - " + str(sumRightToLeftDiagonal()) + "| =" ) # print absolute value equation
    print(str(abs(sumLeftToRightDiagonal() - sumRightToLeftDiagonal()))) #print result of absolute difference

# Main
sumLeftToRightDiagonal()
sumRightToLeftDiagonal()
printAbsoluteDifference()

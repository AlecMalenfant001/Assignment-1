# Alec Malenfant amalenf@pnw.edu
# Assignment 1
# Problem 1
import numpy as np

# Define input functions
def inputNumRowsCols():
    R = int(input("Enter the number of rows & columns: "))
    if R > 99:
        print("Error : The number of rows & columns cannot exceed 99")
        inputNumRowsCols()
    elif R <= 0:
        print("Error : The number of rows & columns must be greater than 0")
    else:
        return R



# Row wise user data input
def userMatrixInput(numRows, numCols):
    matrixArray = [] # Array to be converted into matrix
    print("Please enter each row as a line of integers separated by a space")
    # Input data
    for i in range(numRows):
        matrixArray.append(input("Enter row " + str(i+1) + " : ").split())
        # Check the input matches the correct format
        if len(matrixArray[i]) != numCols:
            print("Error : number of columns does not match desired value")
            waitToKill()



    matrix = np.matrix(matrixArray).astype(int) # Convert to numpy matrix
    return matrix

# Get sum of left-to-right diagonal
def sumLeftToRightDiagonal(matrix):
    return np.trace(matrix)

# Get Sum of right-to-left diagonal
def sumRightToLeftDiagonal(matrix):
    flippedMatrix = np.fliplr(matrix)
    return np.trace(flippedMatrix)

# Get absolute difference of diagonals
def printAbsoluteDifference(matrix):
    print("|" + str(sumLeftToRightDiagonal(matrix)) + " - " + str(sumRightToLeftDiagonal(matrix)) + "| = " + # absolute difference equation
    str(abs(sumLeftToRightDiagonal(matrix) - sumRightToLeftDiagonal(matrix)))) # absolute difference result

def waitToKill():
    # Wait for user input to kill the running program
    input("Press enter to quit ")
    quit()

def main():
    numRowsCols = inputNumRowsCols()
    matrix = userMatrixInput(numRowsCols, numRowsCols) #we are only using square matricies, so the same value is passed twice
    print(matrix)
    printAbsoluteDifference(matrix)
    waitToKill()

if __name__ == "__main__":
    main()

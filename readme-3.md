# Intro to AI Assignment-1 Problem-3

# By Alec Malenfant

# Overview

For this program, we will be working with [this](https://archive.ics.uci.edu/dataset/53/iris) This program converts a .data file to a .csv file and then creates a scatter plot to represent the data in the file.

## Data Representation Explanation

Petal Width will be compared with Petal Length in a scatter plot to classify Iris plant species. I believe that this representation of the data best explains the features of the dataset because of how the clearly the different species are classified. Iris-setosa is represented by red dots in the bottom left corner, which have a small petal width and small petal length. Iris-versicolor is depicted by dots in the middle of the scatter plot with a moderate petal width and moderate petal length. Finally, Iris-virginica is represented as blue dots in the top right of the scatter plot with a high petal width and a high petal length.

## Running the Program

To run this program, open with Python. No other user input should be required. After running, the Python program will open a console. Then, the program will display the new scatter plot in a new window.
<br/>To close the program, close the scatter plot window and hit enter on the console to quit the program.
<br/>An 'iris.data' file is **not necessary** to run this progam. In the case that this file is missing, the program will print an error to the console, but will not crash. However, if an 'iris.data' file is *not* in the root directory of the .py program, a file labeled 'iris.data' **must** be supplied instead. This file should include *at least* these three columns :

* petal length

* petal width

* species
  <br/>
  These columns **are case sensitive**

## Converting .data to .csv

The 'iris.data' file from the dataset will be automatically converted into a .csv file named 'iris.csv'. This .data file should be in the same root directory as Assignment01-Problem03.py. The new 'iris.csv' file will be where the rest of the program gets the data to be displayed.

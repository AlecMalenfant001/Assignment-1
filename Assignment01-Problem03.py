# Alec Malenfant amalenf@pnw.edu
# Assignment 1
# Problem 3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

#convert .data to .csv
with open('iris.data', 'r') as in_file:
    with open ('iris.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('septal length', 'septal width', 'petal length', 'petal width', 'species')) #column titles
        reader = csv.reader(in_file)
        for row in reader:
            writer.writerow(row)

# Create scatter plot for septals
septalLength = pd.read_csv('iris.csv', usecols=['septal length'])
septalWidth = pd.read_csv('iris.csv', usecols=['septal width'])

#create and display scatter plot
plt.scatter(septalLength, septalWidth)
plt.title("Septal Length v Septal Width")
plt.xlabel("Septal Length")
plt.ylabel("Septal Width")
plt.show()


# Create scatter plot for petals
petalLength = pd.read_csv('iris.csv', usecols=['petal length'])
petalWidth = pd.read_csv('iris.csv', usecols=['petal width'])

#create and display scatter plot
plt.scatter(petalLength, petalWidth)
plt.title("Petal Length v Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
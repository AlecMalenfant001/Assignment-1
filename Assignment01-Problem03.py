# Alec Malenfant amalenf@pnw.edu
# Assignment 1
# Problem 3
# This program will plot Petal Length to Petal Width according to the iris data set
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import traceback
import csv
import os

# Change working directory to the path of this python file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#convert .data to .csv
try:
    with open('./iris.data', 'r') as in_file:
        with open('./iris.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('septal length', 'septal width', 'petal length', 'petal width', 'species')) #column titles
            reader = csv.reader(in_file)
            for row in reader:
                writer.writerow(row)
except FileNotFoundError:
    print("Error : There is no 'iris.data' file to convert to .csv")
    print(traceback.format_exc())
except Exception as e:
    print(traceback.format_exc())

#Plot Data from .csv
try:
    # Load the Iris dataset
    iris = pd.read_csv('./iris.csv')

    # Extract data
    petal_length = pd.read_csv('./iris.csv', usecols=['petal length'])
    petal_width = pd.read_csv('./iris.csv', usecols=['petal width'])
    species = pd.read_csv('./iris.csv', usecols=['species'])['species'].values

    # Define colors for each species
    colors = {"Iris-setosa": "red", "Iris-versicolor": "yellow", "Iris-virginica": "blue"}


    # Create scatter plot with color based on species
    plt.scatter(petal_length, petal_width, c=[colors[specie] for specie in species])
    plt.title("Petal Length vs Petal Width by Species")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")

    # Create custom legend entries
    handles = [mpl.patches.Patch(color=color, label=label) for label, color in colors.items()]
    # Add a legend
    plt.legend(handles=handles)
    #Display scatter plot
    plt.show()

except FileNotFoundError:
    print("Error : 'iris.csv' not found")
    print(traceback.format_exc())
except Exception as e:
    print(traceback.format_exc())

# Wait for user input to kill the running program
input("Press enter to quit ")
quit()
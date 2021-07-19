#This app creates a simple program for using dictionaries to store and process
# the contents of a very popular dataset, the Iris flower dataset.
#The Iris flower dataset is one of the most popular datasets in human history. 
# The dataset contains 3 classes of 50 instances each, where each class refers 
# to a type of iris plant: setosa, virginica, or versicolor. For each sample, 
# 4 attributes are stored: petal length, petal width, sepal length, and sepal width.
#Name: Ruth Betancourt
#Class: COP4045
#Assignment: A#5
#Instructor: Dr. Marques

import csv
import matplotlib


def calculateAvg(dataLines):
    # Declare sum values for each species
    # First is petal length
    # Second is petal width
    # Third is sepal length
    # Fourth is sepal width
    sumAttribs = {
        "setosa": [0, 0, 0, 0],
        "versicolor": [0, 0, 0, 0],
        "virginica": [0, 0, 0, 0]
    }

    counts = {
        "setosa": 0,
        "versicolor": 0,
        "virginica": 0
    }

    # read lines from dataLines
    for row in dataLines:
        species = row[-1] # get the species
        # add the columns
        sumAttribs[species][0] += float(row[2])
        sumAttribs[species][1] += float(row[3])
        sumAttribs[species][2] += float(row[0])
        sumAttribs[species][3] += float(row[1])
        # increase count
        counts[species] += 1
  
    # calculate and return a dict of averages
    avgs = {
        species: [x / counts[species] for x in sumAttribs[species]] for species in sumAttribs
    }

    # return avgs
    return avgs

def prettyPrint(avgs):
    # pretty print function
    print("This program computes summary statistics for the Iris Dataset\n")
    print('---------------------------------------------------------------------------------')
    print(f'{"Species":<20} {"Setosa":>10} {"Versicolor":>20} {"Virginica":>20}')
    print('---------------------------------------------------------------------------------')
    print("Attributes (cm):")
    print(f'{" Avg petal length:":<20} {avgs["setosa"][0]:>10.2f} {avgs["versicolor"][0]:>20.2f} {avgs["virginica"][0]:>20.2f}')
    print(f'{" Avg petal width:":<20} {avgs["setosa"][1]:>10.2f} {avgs["versicolor"][1]:>20.2f} {avgs["virginica"][1]:>20.2f}')
    print(f'{" Avg sepal length:":<20} {avgs["setosa"][2]:>10.2f} {avgs["versicolor"][2]:>20.2f} {avgs["virginica"][2]:>20.2f}')
    print(f'{" Avg sepal width:":<20} {avgs["setosa"][3]:>10.2f} {avgs["versicolor"][3]:>20.2f} {avgs["virginica"][3]:>20.2f}')

# main script
# open file for reading
with open('iris.csv', 'r') as dataFile:
    reader = csv.reader(dataFile)
    # skip the header line
    next(reader)
    data = []
    # add all data
    for row in reader:
        data.append(row)

# calculate avgs
avgs = calculateAvg(data)
prettyPrint(avgs)

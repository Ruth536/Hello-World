import csv   #importing required module
import matplotlib.pyplot as plt# importing required module

#FUNCTION DEFINITION
#highest mileage data
#from http://www.fueleconomy.gov/FEG/download.shtml
def create_mileage_list(epa_file): 
    #create a list of cars and mileage from epa_file
    #create a mileage list and initialize it to empty
    mileage_list = []
    epa_file.readline()
    x, y = [], []
    
    for line in epa_file(x,y): # get each line from the file
        line_list = line.split(',')# csv split on comma
        if 'Car' in line_list[70]: # append highway mileage
            mileage_list.append(int(line_list[10]))
    return mileage_list
    
'''def create_mileage_list2(epa_file):
    mileage_list = []
    epa_file.readline()   #skip header line
    for line in epa_file:
        line_list = line.split(',')
        if 'Car' in line_list[70]:
            mileage_list.append((int(line_list[10]), line_list[2], line_list[3]))
    return mileage_list'''

def find_max_min_mileage(mileage_list, max_mileage, min_mileage):
    
    max_mileage_list = []
    min_mileage_list = []


    for car_tuple in mileage_list:
        if car_tuple[0] == max_mileage:
            max_mileage_list.append(car_tuple)
        if car_tuple[0] == min_mileage:
            min_mileage_list.append(car_tuple)
            
    return max_mileage_list, min_mileage_list


def create_mileage_list(epa_file):
    
    mileage_list = []
    reader = csv.reader(epa_file) #create csv reader
    for line_list in reader:      #no split needed
        mileage_list.append(line_list[10])
    return mileage_list
        
        
#PLOTTING EPA DATA         

fp = open("epadata2015.csv")
fp = open("epadata2020.csv")
x,y = [], []
epa_plot = ''

for line in fp:
    line_lst = line.strip().split()
    x.append(str([1])) # year
    y.append(str([2]))  # unadjusted highway MPG Average

fp.close()
#plotting the points
plt.plot(x, y)
plt.ylabel("Highway MPG Average")  #naming y axis
plt.xlabel("Year")         #naming x axis
plt.title("EPA Annual Highway MPG Average")#Giving a title to my graph

#function to show the plot
plt.show()
    #save file
plt.savefig(f"{epa_plot.png}")
savePlot = []
savefig = {}
if (savePlot == 's'):
    savefig('epa_plot.png')
else:
    plt.show()

run = str(input("Press any key to exit  or 'y' to run again: ")).lower()
    
#epa_file = open("mileage_list.txt", "r")

# *********************************************************************************************
# DRIVER 

'''This application uses data from the US Environment Protection agency (EPA)
to generate an EPA vehicle fuel consumption information and the relevant trends over time.'''

print("Welcome to Vehicle Fuel Consumption Information!\n")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>")

option = input(" 1: Mileage Information\n 2: Trend over time\n Please enter your selection: ")

#open EPA data file object
epa_file = open("epadata2015.csv", "r")
epa_file = open("epadata2020.csv", "r")
mileage_list = create_mileage_list(epa_file)


if (option == 1):
        input("Please enter MPG interval: \n")

print("\nMake | Model\n")
if (option == 2):
       input("Please enter Measure: ")
print("Plot trend over time\n")


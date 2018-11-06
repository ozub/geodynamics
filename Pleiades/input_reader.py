import sys
import os
import numpy as np

# To run this: python input_reader.py <directory>

# Record root directory entered into the argument (Maybe add if/else for 2nd argument)
rootdir = str(sys.argv[1])

# Create list of subdirectories inside of the specified root directory
# Maybe Try to clean this up here.. Could include rootdir + dirlist all in one. 
dirlist = []
for root, dirs, files in os.walk(rootdir):
    dirlist += dirs

# Print out the list if needed to double check
# print(dirlist)


# Function that extracts values from main_input
def extract_input(filename):
    infile = open(filename, 'r')
    infile.readline()
    name = []
    value = []
    equal = "="
    records = ["rmin","rmax","luminosity","pressure_specific_heat","nu_top","kappa_top"]

    for line in infile:
        for i in records:
            if i in line:
                line = line.strip()
                line = line.replace(' ','')
                line = line.replace('d','e')
                a = line.split("=")
                name.append(a[0])
                value.append(a[1])

    infile.close()
    value = list(map(float, value))
    
    # Print main_input values
    rmin = value[0]
    rmax = value[1]
    luminosity = value[2]
    psh = value[3]
    nu = value[4]
    kappa = value[5]

    print(records[0] + ": " + str(rmin))
    print(records[1] + ": " + str(rmax))
    print(records[2] + ": " + str(luminosity))
    print(records[3] + ": " + str(psh))
    print(records[4] + ": " + str(nu))
    print(records[5] + ": " + str(kappa))

    return name, value

# Loop over several subdirectories and extract values from each main_input file.
for i in dirlist:
    os.chdir(rootdir + "/" + i)
    print()
    print("Working directory: " + os.getcwd())
    # Extract by calling definition above
    extract_input('main_input')
    print()
    print("-------------------")

import sys
import os
import numpy as np

# Record directory entered into the argument (Maybe add if/else for 2nd argument)
directory = str(sys.argv[1])
# print(directory)

# Loop over several directories (Test later)
# for i in range(0,5):
    # print(directory + 'case' + str(i))
    # os.chdir(directory + 'case' + str(i))

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

extract_input('main_input')
    

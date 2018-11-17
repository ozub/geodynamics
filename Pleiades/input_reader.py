import sys
import os
import numpy as np
from rayleigh_diagnostics import ReferenceState, build_file_list
from rayleigh_diagnostics import Shell_Avgs, build_file_list



# To run this: python input_reader.py <directory> && Include rayleigh_diagnostics.py on the same path where this is run from

# Record root directory entered into the argument (Maybe add if/else for 2nd argument)
rootdir = str(sys.argv[1])

# Create list of subdirectories inside of the specified root directory
# Maybe Try to clean this up here.. Could include rootdir + dirlist all in one. 
dirlist = []

# Need to fix, so that it only adds directories into the list and not subdirectories inside of the directories.
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
    records = ["rmin","rmax","luminosity","pressure_specific_heat","nu_top","kappa_top","angular_velocity"]

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
    cp = value[3]
    nu = value[4]
    kappa = value[5]
    omega = value[6]

    print(records[0] + ": " + str(rmin))
    print(records[1] + ": " + str(rmax))
    print(records[2] + ": " + str(luminosity))
    print(records[3] + ": " + str(cp))
    print(records[4] + ": " + str(nu))
    print(records[5] + ": " + str(kappa))

    return rmin, rmax, luminosity, cp, nu, kappa, omega

# Loop over several subdirectories and extract values from each main_input file.
for i in dirlist:
    os.chdir(rootdir + "/" + i)
    print()
    print("Working directory: " + os.getcwd())

    # Define variables
    rmin, rmax, luminosity, cp, nu, kappa, omega = extract_input('main_input') 
 
    b = ReferenceState(filename='', path='reference')
    # Change values to get Shell_Avgs at different times
    files = build_file_list(400000,500000, path='Shell_Avgs')
    c = Shell_Avgs(filename=files[0], path='')

    nfiles = len(files)

    nr = c.nr
    nq = c.nq 
    nmom = 4
    niter = c.niter
    radius = c.radius
    savg = np.zeros((nr,nmom,nq),dtype='float64')
    for i in range(niter):
        savg[:,:,:] += c.vals[:,:,:,i]
    savg = savg*(1.0/niter)

    lut = c.lut
    ftwil = lut[1433]
    eflux = lut[1440]
    enthflux = lut[1455]
    keflux = lut[1923]

    fpr = 4.0*np.pi*radius*radius

    ftwilelum = savg[:,0,ftwil]
    elum = savg[:,0,eflux]
    enthlum = savg[:,0,enthflux]
    kelum = savg[:,0,keflux]

    # Reverse lists and radius list
    ftwarray = ftwilelum[::-1]
    revr = radius[::-1]
    relum = elum[::-1]
    renthlum = enthlum[::-1]
    rkelum = kelum[::-1]

    h = rmax - rmin
    
    ##### Integration Steps
    normaliz = np.trapz(revr**2, revr)
    # Print volume to doulbe check
    # print("Volume: " + str(4*np.pi*normaliz))

    # Solve g-twidle
    g = np.trapz(b.gravity*revr**2, revr)/normaliz
    # print("Gravity: " + str(g))

    # Solve rho-twidle
    rho = np.trapz(b.density*revr**2, revr)/normaliz

    # Solve temperature-twidle
    temperature = np.trapz(b.temperature*revr**2, revr)/normaliz

    # Integrate FQ
    fq = (np.trapz(ftwarray*revr**2, revr))/normaliz

    # Integrate FL
    fl = np.trapz((luminosity/(4*np.pi*revr**2))*revr**2, revr)/normaliz

    # Integrate KE Flux
    fk = np.trapz(rkelum*revr**2, revr)/normaliz

    # Integrate Enthelpy Flux 
    fe = np.trapz(renthlum*revr**2, revr)/normaliz

    # Integrate Convective flux
    fc = np.trapz(relum*revr**2, revr)/normaliz

    # Solve for Rayleigh Number
    ra = (g*(fl-fq)*h**4)/(cp*rho*temperature*nu*kappa**2)
    print("ra = " + str(ra))

    # Solve Nusselt Number
    nusselt = (fk+fe+fq)/fl
    print("Nusselt = " + str(nusselt))

    # Solve Ekman Number
    ek = nu/(omega*h**2)
    print ("Ekman = " + str(ek))

    


    print()
    print("-------------------")

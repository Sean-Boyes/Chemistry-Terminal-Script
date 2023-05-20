# Importing library
import Chem_Constants
import P_Table

# To-Do
# maybe replace none with 'x' to be less confusing and more straightforward
# need recursive check

# ~Chem Equations~ #

def getPressure(volume = None,n = None, temp = None):
    if (volume == None):
        # get volume function
        return 0
    if (n == None):
        # get mole function
        return 0
    if (temp == None):
        # get temp function
        return 0
    # Run when all variables need are acquired 
    if (temp != None) and (n != None) and (volume != None):
        return ( (n * Chem_Constants.R_atm * temp) / (volume) ) # temp is in kelvin*

def getVolume(density = None, mass = None, temp = None, n = None, pressure = None):
    if (density == None):
        # get density function
        return 0
    if (mass == None):
        # get mass function
        return 0
    if (temp == None):
        # get temp function
        return 0
    if (n == None):
        # get n function
        return 0 
    if (pressure == None):
        getPressure()
    
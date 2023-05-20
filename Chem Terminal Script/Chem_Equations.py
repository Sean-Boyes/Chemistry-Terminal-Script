# Importing library
from Chem_Numbers import *
import P_Table

# To-Do
# maybe replace none with 'x' to be less confusing and more straightforward
# need recursive check

# ~Chem Equations~ #

def get_pressure() -> (int):
    if (variable.volume == None):
        # get volume function
        return 0
    if (variable.n == None):
        # get mole function
        return 0
    if (variable.temp == None):
        # get temp function
        return 0
    # Run when all variables need are acquired 
    if (variable.temp != None) and (variable.n != None) and (variable.volume != None):
        return ( (variable.n * R_atm * variable.temp) / (variable.volume) ) # temp is in kelvin*

def get_volume() -> (int):
    if (variable.density == None):
        # get density function
        return 0
    if (variable.mass == None):
        # get mass function
        return 0
    if (variable.temp == None):
        # get temp function
        return 0
    if (variable.n == None):
        # get n function
        return 0 
    if (variable.pressure == None):
        get_pressure()
    
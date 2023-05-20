# Importing libraries
from Chem_Numbers import *
import P_Table
import Chem_Conversions
import Chem_Equations
        
# thisIsVariable 
# this_is_function

# lists for commands and variables

def message_handeler(userInput):
    userInput = userInput.split(" ")
    if userInput.count("=") == 0:
        # input is command
        print("is command")
    else:
        while userInput.count("=") != 0:
            # remove all instances of '='
            userInput.pop(userInput.index("="))
        # 

# Testing

message = "What variables do you have? \n"
message += "volume (v) \n"
message += "moles (n) \n"
message += "temp (t) \n"
message += "density (d) \n"
message += "mass (m) \n"
message += "pressure (p) \n"
print(message)

message_handeler(input(""))

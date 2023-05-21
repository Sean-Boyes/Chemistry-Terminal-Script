# Importing libraries
from Chem_Numbers import *
import P_Table
import Chem_Conversions
import Chem_Equations
from Input_Handler import *
        
# thisIsVariable 
# this_is_function

# Initial message at start up
print("\n")
message = "What variables do you have? \n"
message += "volume (v) \n"
message += "moles (n) \n"
message += "temp (t) \n"
message += "density (d) \n"
message += "mass (m) \n"
message += "pressure (p) \n"
message += "\nThe syntax is as follows: <variable> = <value> <units> \n"
print(message)

while True:
    message_handeler(get_input())
    Chem_Equations.get_pressure()
    print(pressure.value)

# import lib
from Chem_Numbers import *
from Chem_Equations import *

def get_input()->str:
    return input(">")

def command_handler(command):
    match command:
        case 'exit' | 'e':
            print("exiting...")
            quit()
        case 'help' | 'h':
            message = "commands: \n"
            message += "<exit> or <e> : exits program \n"
            message += "<help> or <h> : shows command list \n"
            print(message)
        case _:
            print("Error: Command not Found")
            return
        
def variable_handler(variable, value):
    match variable:
        case "v":
            volume.value = value
        case "n":
            n.value = value
        case "t":
            temp.value = value
        case "d":
            density.value = value
        case "m":
            mass.value = value
        case "p":
            pressure.value = value
        case _:
            print("Error: variable %s not found", variable)
    
def message_handeler(userInput):
    if userInput.count("=") == 0:
        # input is command
        command_handler(userInput)
        return
    else:
        userInput = userInput.split(" ")
        # Clean the input
        while userInput.count("=") != 0:
            # remove all instances of '='
            userInput.pop(userInput.index("="))
        
        # There has to be a better way...
        while len(userInput) > 0:
            variable_handler(userInput[0],userInput[1])
            userInput.pop(0)
            userInput.pop(0)      
        
        get_pressure()
        print(pressure.value)
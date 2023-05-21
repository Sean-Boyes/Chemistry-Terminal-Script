# ~Chem Conversions~ #
import Chem_Numbers

# Pressure 
def pressure_Convert(pressure, unit):
    match unit:
        case "atm":
            return pressure
        case "kPa":
            return (pressure / 101.3)
        case "mmHg" | "torr":
            return (pressure / 760)
        case "psi":
            return (pressure / 14.1)
        case _:
            print("Not a valid pressure unit")
            return False
        
# Temperature
def temp_Covert(temp, unit):
    match unit:
        case "K":
            return temp
        case "C":
            return (temp / + 273)
        case "F":
            return ((temp - 32) * (5/9) + 273) 
        case _:
            print("Not a valid temperature")
            return False
        
# Volume
def volume_Convert(volume, unit):
    match unit:
        case "L":
            return volume
        case "mL":
            return (volume / 1000)
        case "cm": # cm^3 to meters^3
            return (volume / 1000)
        case _:
            print("Not a valid volume")
            return False
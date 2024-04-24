def sheetToPound(x):
    x = x / 100
    x = int(round(x, 3))
    return x

def woodUse(x):
    x = x * 4
    return x

def totalEnergy(x): # don't forget it's BTU and million after
    x = ((x / 100) * 12.7) / 10
    x = round(x, 2)
    return x

def GHGEmissions(x):
    x = x * 9
    x = int(round(x, 3))
    return x

def waterUse(x): # it's in gallons
    x = x * 10.7
    x = int(round(x, 3))
    return x

def solidWaste(x):
    x = x * 0.588
    x = int(round(x, 3))
    return x
 # I've decided to keep imperial units. Maybe someone outside metric system someday will use it. 
def lbsToKg(x):
    x = x * 0.45359237
    x = int(round(x, 3))
    return x

def gallonsToLiters(x):
    x = x * 3.785411784
    x = int(round(x, 3))
    return x

def main():
    pass
#import printerwatchdog
import printerwatchdog_athome
import papercalculator
import time


#
# Please change the settings!
#  BIG NOTE BIG NOTE
#


def timer():
    finalSum = printerwatchdog_athome.scrapData()
    sheetsWeight = papercalculator.sheetToPound(finalSum)
    sheetsWeightKg = papercalculator.lbsToKg(papercalculator.sheetToPound(finalSum))
    woodUse = papercalculator.lbsToKg(papercalculator.woodUse(sheetsWeight))
    totalEnergy = papercalculator.totalEnergy(sheetsWeight)
    GHGEmissions = papercalculator.lbsToKg(papercalculator.GHGEmissions(sheetsWeight))
    solidWaste = papercalculator.lbsToKg(papercalculator.solidWaste(sheetsWeight))
    waterUse = papercalculator.gallonsToLiters(papercalculator.waterUse(sheetsWeight))
    printerwatchdog_athome.writeDB(finalSum, 'Sheets', 'A4Sheet')
    printerwatchdog_athome.writeDB(woodUse, 'WoodUse', 'metrics')
    printerwatchdog_athome.writeDB(totalEnergy, 'TotalEnergy', 'metrics')
    printerwatchdog_athome.writeDB(GHGEmissions, 'GHGEmissions', 'metrics')
    printerwatchdog_athome.writeDB(solidWaste, 'SolidWaste', 'metrics')
    printerwatchdog_athome.writeDB(waterUse, 'WaterUse', 'metrics')    
    print('Cooling down...')


while True:
    print('Resuming...')
    timer()
    time.sleep(120)


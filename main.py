import printerwatchdog
import papercalculator
import time

def timer():
    finalSum = printerwatchdog.scrapData()
    sheetsWeight = papercalculator.sheetToPound(finalSum)
    sheetsWeightKg = papercalculator.lbsToKg(papercalculator.sheetToPound(finalSum))
    woodUse = papercalculator.lbsToKg(papercalculator.woodUse(sheetsWeight))
    totalEnergy = papercalculator.totalEnergy(sheetsWeight)
    GHGEmissions = papercalculator.lbsToKg(papercalculator.GHGEmissions(sheetsWeight))
    solidWaste = papercalculator.lbsToKg(papercalculator.solidWaste(sheetsWeight))
    waterUse = papercalculator.gallonsToLiters(papercalculator.waterUse(sheetsWeight))
    printerwatchdog.writeDB(finalSum, 'Sheets', 'A4Sheet')
    printerwatchdog.writeDB(woodUse, 'WoodUse', 'metrics')
    printerwatchdog.writeDB(totalEnergy, 'TotalEnergy', 'metrics')
    printerwatchdog.writeDB(GHGEmissions, 'GHGEmissions', 'metrics')
    printerwatchdog.writeDB(solidWaste, 'SolidWaste', 'metrics')
    printerwatchdog.writeDB(waterUse, 'WaterUse', 'metrics')    
    print('Cooling down...')


while True:
    print('Resuming...')
    timer()
    time.sleep(120)


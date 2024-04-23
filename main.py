import printerwatchdog
import time

def timer():
    printerwatchdog.writeDBFinalSum()
    print('Cooling down...')


while True:
    print('Resuming...')
    timer()
    time.sleep(120)


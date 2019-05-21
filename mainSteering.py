import time
from math import sqrt
from math import ceil
from math import floor
from math import atan
from newCompass import *
from mainGPS import *
from rudderMovement import *
from windCalculations import *

def mainSteering(dx, dy): # Destination coords
    #print("Real Angle", (360 - getBearing() + 90)  % 360)
    bearing = (360 - getBearing()+ 90) % 360
    print("True Bearing", getBearing())
    y, x = getGPS() #int(input("Y for us: ",)), int(input("X for us:")) # Will be our GPS coords
    print("Our coords: ", x, y)
    print("Dest coords: ", dx, dy)
    if((dx - x) != 0):
        print("Real angle: ", bearing)
       #get the right dest angle, using tan-1()
        destinationAngle = atan( (dy - y) / (dx - x) ) * 180 / 3.14159
        print("Dest angle: ", destinationAngle)
        difference = (bearing - destinationAngle) % 360
        print("Real difference: ", difference)
        if(difference < 180):
            print("Smaller than 180. Going, ", difference)
            moveRudder(ceil(-difference / 15))
        elif(difference >= 180):
            print("Bigger than 180. Going: ", 360-difference)
            moveRudder(floor((360 - difference) / 15))
        time.sleep(0.25)

if __name__ == "__main__":
    #dx = float(input("Latitude: "))
    #dy = float(input("Longitude: "))
    if input("Predetermined? ") == "no":
        actualX = [float(input("Actual X: "))] #60.1042,60.1048, 60.1045, 60.1042]
        actualY = [float(input("Actual Y: "))] #19.949, 19.949, 19.95, 19.949]
        dxs = [float(input("Overshooting X: "))] #60.1042, 60.1056, 60.1039, 60.1042]
        dys = [float(input("Overshooting Y: ")) ] #19.951, 19.949, 19.948, 19.951]
    else:
       actualX =[60.105031, 60.104893, 60.104871]
       actualY =[19.946171, 19.945834, 19.946205]
       dxs = [60.105185, 60.104767, 60.104877]
       dys = [19.946151, 19.945548, 19.946616]

    index = 0
    startTime = time.time()
    print("Mission start!")
    iteration = 0
    while(1):
        iteration += 1
        print("\n Iteration: ", iteration, "\n Mission time: ", round(time.time()-startTime))

        mainSteering(float(dys[index]), float(dxs[index]))
        #mainSteering(float(dy), float(dx))
        time.sleep(3)
        analyzeWind()
        x, y = getGPS()
        distance = 100000 * sqrt( (x - actualX[index]) ** 2 + (y - actualY[index]) ** 2)
        print("Distance to actual destination: ", distance)

        if distance < 25:
            index += 1
            index %= len(actualX)
            print("Success.")
            print("Next point.\n\n")

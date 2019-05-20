import time
from math import ceil
from math import floor
from math import atan
from newCompass import *
from mainGPS import *
from rudderMovement import *

def mainSteering(dx, dy): # Destination coords
    #print("Real Angle", (360 - getBearing() + 90)  % 360)
    bearing = (360 - getBearing()+ 90) % 360
    print("\n True Bearing", getBearing())
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
    x = input("Latitude: ")
    y = input("Longitude: ")
    while(1):
        mainSteering(float(y), float(x))

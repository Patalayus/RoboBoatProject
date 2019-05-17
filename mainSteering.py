import time
from math import ceil
from math import floor
from math import tan
from compass import *
from mainGPS import *
from rudderMovement import *

def mainSteering(dx, dy): # Destination coords
    bearing = readCompass()
    realBearing = realAngle(bearing)
    y, x = 51, -1.50 # Will be our GPS coords
    if((dx - x) != 0):
        destinationAngle = tan( (dy - y) / (dx - x) )
        difference = realBearing - destinationAngle
        print(difference)
        if(difference < 180):
            moveRudder(ceil(-difference / 45))
        elif(difference >= 180):
            moveRudder(floor(-(180 - difference) / 45))
        time.sleep(1)

if __name__ == "__main__":
    while(1):
        mainSteering(46, -75)

from moveSail import *
from rudderMovement import *
from newCompass import *
import random
import time

#get wind from mqtt
def tacking():
	if 'lastTack' not in tacking.__dict__:
		tacking.lastTack = -1
	else:
		tacking.lastTack *= -1
	#move rudder in the direction of lastTack
	#disable other code
	moveRudder(6 * tacking.lastTack)
	print("Rudder moved, ", tacking.lastTack)
	#print("Sail moved to middle")
	time.sleep(17)
	print("tacking stopped")

def analyzeWind():
	windDegree = 0
	print("Current wind: ", windDegree)

	compassBearing = getBearing() #pointed east

	difference = (windDegree - compassBearing) % 360

	if difference > 180:
		difference = (360-difference)

	print("Diff: ", difference)

	if difference > 140: #180 +- 30
		#we are in irons
		print("In irons")
		moveSail(-9)
		tacking()
	elif difference > 40:
		#wind from the side
		print("From the side")
		moveSail(-6)
	else:
		#wind from behind
		print("From behind")
		moveSail(-3)

if __name__ == "__main__":
	while True:
		analyzeWind()
		input()


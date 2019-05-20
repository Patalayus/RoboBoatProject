#from moveSail import *
#from newCompass import *
import random

#get wind from mqtt
def tacking():
	if 'lastTack' not in startTacking.__dict__:
		lastTack = -1
	else:
		lastTack *= -1
	#move rudder in the direction of lastTack
	#disable other code
	#sleep 5 seconds
	#release sail to 45
	#sleep 5
	#let everything else take over

def analyzeWind():
	windDegree = random.randint(0,360) #will be given by weather station
	print("Current wind: ", windDegree)

	compassBearing = 90 #pointed east

	difference = windDegree - compassBearing


	if difference > 180:
		difference = (360-difference)

	if difference > 140: #180 +- 30
		#we are in irons
		#tacking
		#sail at 0 degrees
		lastTack = startTacking(lastTack)
	elif difference > 40:
		#wind from the side
		#45 degrees
	else:
		#wind from behind
		#90 degrees, max

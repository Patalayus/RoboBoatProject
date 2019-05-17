import pigpio

def moveSail(value):
	"""Moves sail based on [0, 5], 0=8cm, 5=42cm """
	gpio = pigpio.pi()
	gpio.set_mode(18, pigpio.OUTPUT)
	gpio.hardware_PWM(18, 50, 1000000 - (76750 + 4650 * value))

if __name__ == "__main__":
	while(1):
		try:
			moveSail(int(input("Enter [0,5]: ")))
		except KeyboardInterrupt:
			gpio=pigpio.pi()
			gpio.set_mode(18, pigpio.OUTPUT)
			gpio.hardware_PWM(18, 50, 0)
			exit()

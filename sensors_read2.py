import Adafruit_DHT, Adafruit_BMP.BMP085 as Sensor2
import time
import sys

sensor1 = Adafruit_DHT.DHT22
sensor1_pin = 22
sensor2 = Sensor2.BMP085()
while True:
	try:
		humidity, temperature = Adafruit_DHT.read_retry(sensor1, sensor1_pin)
		pressure = sensor2.read_pressure()
		temp = sensor2.read_temperature()
		altitude = sensor2.read_altitude()

		if humidity and temperature:
			print('[SENSOR 1] Humidity: {0:0.1f}  % ---- Temperature: {1:0.1f} *C\n'.format(humidity, temperature).center(100))
		else:
			print("[SENSOR 1] Failed to get a reading")
		if pressure and temp and altitude:
			print("[SENSOR 2] Pressure: {0:0.1f} Pa ---- Temperature: {1:0.1f} *C ---- Altitude: {0:0.1f} m\n".format(pressure, temp,altitude).center(100))
		else:
			print("[SENSOR 2] Failed to get a reading")
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit()

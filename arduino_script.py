import serial
import time
import sys
import sqlite3
from datetime import datetime

class Arduino:
	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 9600)
		self.ser.baudrate = 9600

	def read_data(self):
		try:
			read_ser = self.ser.readline()
			print(str(read_ser))
			return read_ser
		except:
			print("Something went wrong")

	def write_data(self, data):
		try:
			connection = sqlite3.connect('database.db')
			cursor = connection.cursor()
			cursor.executescript("INSERT INTO soil(date_measured, soil_moisture) VALUES('{}', {});".format(datetime.now(), data))
			connection.commit()
		except sqlite3.Error:
			print("Something went wrong")
			if connection:
				print("Rolling back!")
				connection.rollback()
		except:
			print("Putangina")
			sys.exit()
		finally:
			if connection:
				connection.close()
if __name__ == '__main__':
	while True:
		try:
			arduino = Arduino()
			data = arduino.read_data()
			arduino.write_data(data)
			time.sleep(1)
		except KeyboardInterrupt:
			sys.exit()
#	print(a)

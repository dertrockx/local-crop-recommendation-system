import serial
import sqlite3
import time
import sys
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.baudrate=9600

# This function only writes on the database on every item
# In the future, change this to write on the database in a single 'commit' not commit-ing every script
def write_data(data):
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	cursor.executescript("INSERT INTO soil(date_measured, soil_moisture) VALUES('{}', {});".format(datetime.now(), data))
	connection.commit()

def read_arduino():
	try:
		read_ser = ser.readline()
		print(read_ser)
		return read_ser
		time.sleep(1)
	except KeyboardInterrupt:
		print('\n Bye!')
		sys.exit()
	except:
		print("Something fucked up!")
#for d in range(5):
#	write_data(d)

if __name__ == '__main__':
	while True:
		ard_data = read_arduino()
		write_data(ard_data)
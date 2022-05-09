from time import sleep
from datetime import datetime, timedelta
from pathlib import Path
from orbit import ISS
from sense_hat import SenseHat
import csv
from logzero import logger, logfile

# Define needed functions

def led(sense, location):
    '''Display a message about latitude in the LED of the SenseHat'''
    g = (0,255,0)
    r = (255,0,0)
    if location.latitude.degrees >= 0 and location.longitude.degrees >=0:
        sense.show_message("Latitude: North; longitude: East", text_colour = g, scroll_speed = 0.05) 
    elif location.latitude.degrees >= 0 and location.longitude.degrees < 0:
        sense.show_message("Latitude: North; longitude: West", text_colour = g, scroll_speed = 0.05)
    elif location.latitude.degrees < 0 and location.longitude.degrees < 0:
        sense.show_message("Latitude: South; longitude: West", text_colour = r, scroll_speed = 0.05)
    elif location.latitude.degrees < 0 and location.longitude.degrees >= 0:
        sense.show_message("Latitude: South; longitude: East", text_colour = r, scroll_speed = 0.05)	
   
def create_csv(data_file):
    '''Write header in the created .csv file'''
    with open(data_file, 'w', buffering=1) as f:
        writer = csv.writer(f)
        header = header = ("Counter", "Date/time", "Latitude (deg)", "Longitude (deg)", "Altitude (km)", "yaw", "pitch", "raw", "a_X", "a_Y", "a_Z", "r_X", "r_Y", "r_Z")
        writer.writerow(header)

def add_csv_data(data_file, data):
    '''Add data in a row in the .csv file'''
    with open(data_file, 'a', buffering=1) as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Create a ‘datetime’ variable to store the start time
start_time = datetime.now()

# Create a `datetime` variable to store the current time
now_time = datetime.now()

# Create a 'GPS location' variable
location = ISS.coordinates()

# Activate the sense_nat
sense = SenseHat()


# Create file and directory where to store data
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'
create_csv(data_file)

# Create a logfile
logfile(base_folder/"history.log")

# Initialize a counter
counter = 1

# Run a loop for 180 minutes of experiment 
while (now_time < start_time + timedelta(minutes=176)):
    try:
        # Measure location of ISS
        lat = round(location.latitude.degrees, 2)
        long = round(location.longitude.degrees, 2)
        alt = round(location.elevation.km, 3)
        # Measure movement, acceleration and rotation every 10 s
        orientation = sense.get_orientation()
        yaw = round(orientation['yaw'],4)
        pitch = round(orientation['pitch'],4)
        roll = round(orientation['roll'],4)
        acceleration = sense.get_accelerometer_raw()
        a_x = round(acceleration['x'],4)
        a_y = round(acceleration['y'],4)
        a_z = round(acceleration['z'],4)
        rotation = sense.get_gyroscope_raw()
        r_x = round(rotation['x'],4)
        r_y = round(rotation['y'],4)
        r_z = round(rotation['z'],4)
        data = (
            counter, 
            now_time, 
            lat, 
            long, 
            alt, 
            yaw, 
            pitch, 
            roll,
            a_x, 
            a_y, 
            a_z, 
            r_x, 
            r_y, 
            r_z,
        )
         # Store data in .csv
        add_csv_data(data_file, data)
        # Show message about latitude on LED
        led(sense, location)
        sense.clear()
        # log info
        logger.info(f"Iteration {counter}")
        sleep(10)
        # Update the current time, location and counter
        now_time = datetime.now()
        location = ISS.coordinates()
        counter += 1
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}') 

sense.show_message("Thank you", text_colour = (255,255,255))
sense.clear()
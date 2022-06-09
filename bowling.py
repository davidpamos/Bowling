#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:50:12 2022

@author: Bowling
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file = 'data.csv'

df = pd.read_csv(file,sep=',')
df.head()

yaw = df['yaw'].astype(float)
yaw_list = []
pitch = df['pitch'].astype(float)
pitch_list = []
roll = df['raw'].astype(float)
roll_list = []
altitude = df['Altitude (km)'].astype(float)
a_x = df['a_X'].astype(float)
a_y = df['a_Y'].astype(float)
a_z = df['a_Z'].astype(float)
a = np.sqrt(a_x**2 + a_y**2 + a_z**2)
r_x = df['r_X'].astype(float)
r_y = df['r_Y'].astype(float)
r_z = df['a_Z'].astype(float)
r = np.sqrt(r_x**2 + r_y**2 + r_z**2)

for y in yaw:
    if y>180:
        y = 360-y
    yaw_list.append(y)

longitude = df['Longitude (deg)'].astype(float)
latitude = df['Latitude (deg)'].astype(float)




plt.scatter(longitude,altitude, s=5)
plt.title('ISS altitude (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Altitude (km)',fontsize=10)
plt.savefig('altitude.png')
plt.show()
plt.close()

plt.scatter(longitude,yaw_list, s=5)
plt.title('ISS yaw (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Yaw (deg)',fontsize=10)
plt.savefig('yaw.png')
plt.show()
plt.close()

plt.scatter(longitude,pitch, s=5)
plt.title('ISS pitch (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Pitch (deg)',fontsize=10)
plt.savefig('pitch.png')
plt.show()
plt.close()

plt.scatter(longitude,roll, s=5)
plt.title('ISS roll (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Roll (deg)',fontsize=10)
plt.savefig('roll.png')
plt.show()
plt.close()

plt.scatter(longitude,a, s=5)
plt.title('ISS acceleration (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Acceleration (g)',fontsize=10)
plt.savefig('Acceleration.png')
plt.show()
plt.close()

plt.scatter(longitude,a, s=5)
plt.title('ISS rotation (April 13, 2022)', fontsize = 10)
plt.xlabel('Longitude (deg)',fontsize=10)
plt.ylabel('Gyroscopic rotation',fontsize=10)
plt.savefig('rotation.png')
plt.show()
plt.close()


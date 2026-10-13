#!/usr/bin/env python3

import time
import board
import busio
import adafruit_bmp280
import adafruit_ahtx0

# Initialize I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create BMP280 object
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Optional: set local sea level pressure (hPa)
bmp280.sea_level_pressure = 1013.25

def main():

    aht20 = adafruit_ahtx0.AHTx0(i2c)

    temperature = (bmp280.temperature + aht20.temperature)/2
    pressure = bmp280.pressure
    humidity = round(aht20.relative_humidity)

    print(f"{temperature:.1f} {humidity} {pressure:.2f}")



if __name__=="__main__":
   main()

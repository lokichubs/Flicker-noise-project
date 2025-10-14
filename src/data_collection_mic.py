import time
import csv
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
ads.gain = 1  # Gain=1 for 0-4.096V input range

with open('mic_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'mic_value'])
    for _ in range(86400):  # 24 hours at 1 sample/sec
        chan = AnalogIn(ads, ADS1115.P0)  # AIN0
        mic_value = chan.value
        print(f"Mic value: {mic_value}")
        writer.writerow([time.time(), mic_value])
        time.sleep(1)
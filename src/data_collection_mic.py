import Adafruit_ADS1x15
import time
import csv

# Initialize ADS1115
adc = Adafruit_ADS1x15.ADS1115(busnum=1)
GAIN = 1
FSR = 4.096  # Full-scale voltage for gain=1

# Generate filename with timestamp DDMM:HH:MM:SS
file_timestamp = time.strftime("%d%m:%H:%M:%S", time.localtime())
filename = f"mic_data_{file_timestamp}.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'mic_value', 'voltage'])
    print(f"Logging data to {filename}")
    print("Reading ADS1115 values, press Ctrl+C to stop...")

    for _ in range(86400):  # 24 hours at 1 sample/sec
        # Format timestamp as DDMM:HH:MM:SS
        timestamp = time.strftime("%d%m:%H:%M:%S", time.localtime())
        value = adc.read_adc(0, gain=GAIN)
        voltage = (value / 32767) * FSR
        print(f"Timestamp: {timestamp}, Raw: {value}, Voltage: {voltage:.4f} V")
        writer.writerow([timestamp, value, voltage])
        time.sleep(1)

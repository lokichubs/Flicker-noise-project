import Adafruit_ADS1x15
import time
import csv

# Initialize ADS1115
adc = Adafruit_ADS1x15.ADS1115(busnum=1)
GAIN = 1
FSR = 4.096  # Full-scale voltage for gain=1

# Generate filename-safe timestamp: YYYY-MM-DD_HH-MM
file_timestamp = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
filename = f"mic_data_{file_timestamp}.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp (YYYY-MM-DD-HH-MM-SS)', 'time (s)', 'mic_value (NA)', 'voltage (V)'])
    print(f"Logging data to {filename}")
    print("Reading ADS1115 values, press Ctrl+C to stop...")

    try:
        for i in range(86400):  # 24 hours at 1 sample/sec
            # Format timestamp as "YYYY-MM-DD : HH:MM:SS"
            timestamp = time.strftime("%Y-%m-%d : %H:%M:%S", time.localtime())
            time_sec = i
            value = adc.read_adc(0, gain=GAIN)
            voltage = (value / 32767) * FSR
            # Code below only for debugging purposes - don't want it printing to terminal unless necessary
            #print(f"Timestamp: {timestamp}, Raw: {value}, Voltage: {voltage:.4f} V")
            writer.writerow([timestamp, time_sec, value, voltage])
            time.sleep(1)
    except KeyboardInterrupt:
        print("Logging stopped by user.")

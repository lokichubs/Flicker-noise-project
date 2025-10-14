# Flicker-noise-project
A project that utilizes a Raspi-4 and microphone module to showcase the effect of 1/f or  "flicker" noise. 


## Project Overview
This project demonstrates the measurement and analysis of flicker noise (1/f noise) using a Raspberry Pi 4 and an analog microphone module. Data is collected via an ADS1115 ADC and processed for further analysis.

## Hardware Used
- [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
- [Adafruit ADS1115 ADC](https://www.adafruit.com/product/1085)
- Analog Microphone Module

## Software & Libraries
- Python 3
- [Adafruit CircuitPython ADS1x15 Library](https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15)
- [Adafruit Blinka](https://github.com/adafruit/Adafruit_Blinka)

## Data Collection
The script `data_collection_mic.py` collects timestamped microphone data and saves it to `mic_data.csv` for further analysis.

## Usage
1. Install required libraries:
	```bash
	pip3 install adafruit-circuitpython-ads1x15 adafruit-blinka
	```
2. Connect the hardware as per the datasheets.
3. Run the data collection script:
	```bash
	python3 data_collection_mic.py
	```

## References
- [Wikipedia: Flicker Noise](https://en.wikipedia.org/wiki/Flicker_noise)
- [Adafruit CircuitPython Documentation](https://docs.circuitpython.org/projects/ads1x15/en/latest/)

from machine import Pin, ADC
import time

# --- Hardware Configuration ---
# Power pin for the sensor (New Feature: Corrosion Protection)
sensor_power = Pin(5, Pin.OUT)

# Moisture Sensor
sensor_pin = ADC(Pin(4))
sensor_pin.atten(ADC.ATTN_11DB)

pump_relay = Pin(2, Pin.OUT)

# --- Calibration Thresholds ---
DRY_THRESHOLD = 3000
WET_THRESHOLD = 2000

def pump_on():
    if pump_relay.value() == 0: # Check if not already on
        print("Soil is DRY -> Pump ON")
        pump_relay.value(1)

def pump_off():
    if pump_relay.value() == 1: # Check if not already off
        print("Soil is WET -> Pump OFF")
        pump_relay.value(0)

def get_moisture_level():
    """
    Turns on sensor, takes average readings, turns off sensor.
    Prevents corrosion by not powering the sensor 24/7.
    """
    sensor_power.value(1)       # Power ON
    time.sleep(0.1)             # Wait for stability
    
    readings = []
    for _ in range(10):
        readings.append(sensor_pin.read())
        time.sleep(0.01)
        
    sensor_power.value(0)       # Power OFF (Protection)
    
    average = sum(readings) / len(readings)
    return int(average)

# --- Main Program ---
pump_off()
sensor_power.value(0) # Ensure sensor is off initially
print("Automatic Watering System v2.0 STARTED")

while True:
    current_moisture = get_moisture_level()
    print(f"Current Moisture: {current_moisture}")

    if current_moisture > DRY_THRESHOLD:
        pump_on()
    elif current_moisture < WET_THRESHOLD:
        pump_off()
    
    time.sleep(2)
from machine import Pin, ADC
import time

# --- Hardware Configuration ---
# Moisture Sensor (Connected to Pin 4)
sensor_pin = ADC(Pin(4))
sensor_pin.atten(ADC.ATTN_11DB)  # Full range 0-3.3V

# Pump Relay (Connected to Pin 2)
# 1 = ON, 0 = OFF
pump_relay = Pin(2, Pin.OUT)

# --- Calibration Thresholds ---
DRY_THRESHOLD = 3000  # Above this -> Soil is dry
WET_THRESHOLD = 2000  # Below this -> Soil is wet

def pump_on():
    print("Soil is DRY -> Pump ON")
    pump_relay.value(1)

def pump_off():
    print("Soil is WET -> Pump OFF")
    pump_relay.value(0)

# Ensure pump is off on startup
pump_off()
print("Automatic Watering System STARTED")

while True:
    # Average 10 readings to reduce noise
    readings = []
    for _ in range(10):
        readings.append(sensor_pin.read())
        time.sleep(0.05)
    
    current_moisture = sum(readings) / len(readings)
    print(f"Current Moisture: {int(current_moisture)}")

    # Watering Logic (Hysteresis)
    if current_moisture > DRY_THRESHOLD:
        pump_on()
    elif current_moisture < WET_THRESHOLD:
        pump_off()
    
    time.sleep(1)
    
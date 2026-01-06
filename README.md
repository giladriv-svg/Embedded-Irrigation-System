# Smart Irrigation Control System (ESP32)

An end-to-end embedded solution for automated plant care, implemented using MicroPython.

## Overview
This project demonstrates a closed-loop control system running on an ESP32 microcontroller. It leverages MicroPython for efficient real-time soil moisture monitoring and automated irrigation logic.

## Key Features
* **Firmware:** Written in **MicroPython** for rapid hardware interaction.
* **Control Logic:** Implements a feedback loop based on analog sensor data.
* **Hardware Interface:** PWM signal generation for pump control and sensor calibration.
* **Reliability:** Includes fail-safe mechanisms to handle sensor errors.

## Tech Stack
* **MCU:** ESP32
* **Language:** MicroPython
* **Sensors:** Capacitive Soil Moisture Sensor

## System Architecture

```mermaid
graph TD
    %% Component Definitions
    ESP32[ESP32 Controller]
    Sensor[Capacitive Soil Sensor]
    Transistor[NPN Transistor / BJT]
    Relay[5V Relay Module]
    Pump[Water Pump]
    Power5V[5V Power Source]
    
    %% Sensor Connections (3.3V Logic)
    ESP32 -- "3.3V / GPIO Power" --> Sensor
    Sensor -- "Analog Data (ADC)" --> ESP32
    
    %% Pump Connections (5V Logic via Transistor)
    ESP32 -- "GPIO Control (3.3V)" --> Transistor
    Power5V -- "5V Supply" --> Relay
    Transistor -- "Switch Signal" --> Relay
    Relay -- "High Current Switch" --> Pump
    Power5V -- "Power" --> Pump
    
    %% Styling - Added 'color:#000' for black text
    style ESP32 fill:#f9f,stroke:#333,stroke-width:2px,color:#000
    style Sensor fill:#ccf,stroke:#333,color:#000
    style Relay fill:#ff9,stroke:#333,color:#000
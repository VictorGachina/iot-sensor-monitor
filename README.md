# 🌡️ IoT Sensor Monitor

A Python-based IoT sensor monitoring simulation that collects and analyzes temperature, humidity, and motion data — perfect for construction site monitoring or environmental sensing applications.

## 🚀 Features

- ✅ **Real-time sensor simulation** – Temperature, humidity, motion detection
- ✅ **Alert system** – Triggers notifications when readings exceed thresholds
- ✅ **Data logging** – Stores history of readings
- ✅ **Summary statistics** – Min, max, average after monitoring session
- ✅ **Extensible design** – Easy to adapt for actual hardware

## 🔧 Quick Start

```bash
git clone https://github.com/VictorGachina/iot-sensor-monitor.git
cd iot-sensor-monitor
python sensor_monitor.py

## 📊 Sample Output

🌡️ IoT SENSOR MONITORING SIMULATION
==================================================
🔌 Starting CONSTRUCTION_SITE_01 monitoring...
⏱️ Collecting data for 20 seconds

🚨 [14:23:05] ⚠️ HIGH TEMPERATURE: 31.2°C
📊 [14:23:05] Temp: 31.2°C | Humidity: 45.3% | No motion
📊 [14:23:08] Temp: 28.4°C | Humidity: 52.1% | No motion
🚨 [14:23:11] ⚠️ HIGH HUMIDITY: 72.5%
📊 [14:23:11] Temp: 26.7°C | Humidity: 72.5% | 🚶 MOTION DETECTED
==================================================
📈 MONITORING SUMMARY - CONSTRUCTION_SITE_01
==================================================
Total readings: 7
Temperature range: 24.3°C - 31.2°C
Temperature avg: 27.8°C
Humidity range: 45.3% - 72.5%
Humidity avg: 58.2%

🚨 ALERTS TRIGGERED: 2
[14:23:05] ⚠️ HIGH TEMPERATURE: 31.2°C
[14:23:11] ⚠️ HIGH HUMIDITY: 72.5%


## 🏗️ Real-World Applications

- **Construction site monitoring** – Track concrete curing temperatures, worker safety
- **Environmental monitoring** – Air quality, weather stations
- **Smart building** – HVAC optimization, occupancy detection
- **Equipment health** – Vibration, temperature monitoring for machinery

## 🔌 Integration Options

This script can be adapted for actual hardware:
- Raspberry Pi with DHT22 sensors
- Arduino with temperature/humidity sensors
- Industrial IoT gateways
- Custom API endpoints for cloud storage

## 🛠️ Customization

Modify thresholds in the `check_alerts` method:
```python
if temp > 30.0:  # Change this value for different temperature limits
    alerts.append(f"⚠️ HIGH TEMPERATURE: {temp}°C")


📄 License
MIT License

🤝 Connect
Author: Victor Gachina

GitHub: @VictorGachina

Email: gachinawachira@gmail.com

⭐ Star this repository if you found it useful for your IoT projects!

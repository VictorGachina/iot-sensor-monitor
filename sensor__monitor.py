import random
import time
import datetime
from collections import deque

class SensorMonitor:
    """
    Simulates an IoT sensor monitoring system.
    Collects temperature, humidity, and motion data.
    """
    
    def __init__(self, sensor_id="SENSOR_01"):
        self.sensor_id = sensor_id
        self.temp_history = deque(maxlen=100)  # Keep last 100 readings
        self.humidity_history = deque(maxlen=100)
        self.alerts = []
        
    def read_temperature(self):
        """Simulate temperature reading (15°C to 35°C)"""
        return round(random.uniform(15.0, 35.0), 1)
    
    def read_humidity(self):
        """Simulate humidity reading (30% to 80%)"""
        return round(random.uniform(30.0, 80.0), 1)
    
    def read_motion(self):
        """Simulate motion detection (True/False with 20% chance)"""
        return random.random() < 0.2
    
    def check_alerts(self, temp, humidity):
        """Check if readings trigger alerts"""
        alerts = []
        
        if temp > 30.0:
            alerts.append(f"⚠️ HIGH TEMPERATURE: {temp}°C")
        elif temp < 18.0:
            alerts.append(f"⚠️ LOW TEMPERATURE: {temp}°C")
            
        if humidity > 70.0:
            alerts.append(f"⚠️ HIGH HUMIDITY: {humidity}%")
        elif humidity < 35.0:
            alerts.append(f"⚠️ LOW HUMIDITY: {humidity}%")
            
        return alerts
    
    def collect_data(self, duration_seconds=30, interval=5):
        """
        Collect sensor data for a specified duration.
        
        Args:
            duration_seconds: How long to collect data
            interval: Seconds between readings
        """
        print(f"🔌 Starting {self.sensor_id} monitoring...")
        print(f"⏱️  Collecting data for {duration_seconds} seconds")
        print("-" * 50)
        
        readings_count = 0
        start_time = time.time()
        
        while time.time() - start_time < duration_seconds:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            
            # Read sensors
            temp = self.read_temperature()
            humidity = self.read_humidity()
            motion = self.read_motion()
            
            # Store history
            self.temp_history.append(temp)
            self.humidity_history.append(humidity)
            
            # Check for alerts
            alerts = self.check_alerts(temp, humidity)
            for alert in alerts:
                self.alerts.append((timestamp, alert))
                print(f"🚨 [{timestamp}] {alert}")
            
            # Display reading
            motion_status = "🚶 MOTION DETECTED" if motion else "   No motion"
            print(f"📊 [{timestamp}] Temp: {temp}°C | Humidity: {humidity}% | {motion_status}")
            
            readings_count += 1
            time.sleep(interval)
        
        # Summary
        print("\n" + "="*50)
        print(f"📈 MONITORING SUMMARY - {self.sensor_id}")
        print("="*50)
        print(f"Total readings: {readings_count}")
        
        if self.temp_history:
            print(f"Temperature range: {min(self.temp_history)}°C - {max(self.temp_history)}°C")
            print(f"Temperature avg: {sum(self.temp_history)/len(self.temp_history):.1f}°C")
        
        if self.humidity_history:
            print(f"Humidity range: {min(self.humidity_history)}% - {max(self.humidity_history)}%")
            print(f"Humidity avg: {sum(self.humidity_history)/len(self.humidity_history):.1f}%")
        
        if self.alerts:
            print(f"\n🚨 ALERTS TRIGGERED: {len(self.alerts)}")
            for timestamp, alert in self.alerts[:5]:  # Show last 5 alerts
                print(f"   [{timestamp}] {alert}")
        else:
            print("\n✅ No alerts triggered - all readings normal")
        
        print("="*50)

def main():
    """Run the sensor monitor demo"""
    print("🌡️  IoT SENSOR MONITORING SIMULATION")
    print("="*50)
    
    # Create monitor
    monitor = SensorMonitor("CONSTRUCTION_SITE_01")
    
    # Run for 20 seconds with 3-second intervals
    monitor.collect_data(duration_seconds=20, interval=3)
    
    print("\n💡 Tip: This simulates real IoT sensors on a construction site.")
    print("   Can be extended to work with actual hardware like Raspberry Pi.")

if __name__ == "__main__":
    main()

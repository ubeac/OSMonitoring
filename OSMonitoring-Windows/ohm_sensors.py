import wmi
import _ohm_util as util

#Sensors from Open Hardware Monitor
def get_ohm_sensors():
    import pythoncom
    sensors = []

    pythoncom.CoInitialize()
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")

    sensors_infos = w.Sensor()
    for sensor in sensors_infos:

        #Temperature Sensors
        if sensor.SensorType == "Temperature":
            sensors.append(util.get_temperature(sensor.Name, sensor.Value, sensor.Max))

        #CPU Usage %
        elif sensor.Name == "CPU Total":
            sensors.append(util.get_cpu_usage(sensor.Name, sensor.Value, sensor.Max))

        #Power Consumption
        elif sensor.SensorType == "Power":
            sensors.append(util.get_power(sensor.Name, sensor.Value, sensor.Max))

        #CPU Speed
        elif sensor.SensorType == "Clock":
            sensors.append(util.get_clock(sensor.Name, sensor.Value, sensor.Max))

        #Fan Speed
        elif sensor.SensorType == "Fans":
            sensors.append(util.get_fan_speed(sensor.Name, sensor.Value, sensor.Max))

    return sensors

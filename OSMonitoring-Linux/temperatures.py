import _const as const
from _util import get_sensor
import psutil

def get_temperatures():
    sensors = []

    if not hasattr(psutil, "sensors_temperatures"):
        return sensors
    temps = psutil.sensors_temperatures()
    if not temps:
        return sensors

    for name, entries in temps.items():
        for entry in entries:
            temp_high = entry.high
            temp_crit = entry.critical
            if entry.high == None:
                temp_high = -1
            if entry.critical == None:
                temp_crit = -1
            sensor_name = const.SENSOR_NAME_TEMPERATURE_NAME.format(name, entry.label)
            sensor_value = {
                const.SENSOR_NAME_TEMPERATURE_CURRENT: entry.current,
                const.SENSOR_NAME_TEMPERATURE_HIGH: temp_high,
                const.SENSOR_NAME_TEMPERATURE_CRITICAL: temp_crit
            }
            sensors.append(get_sensor(sensor_name, sensor_value))
            
    return sensors

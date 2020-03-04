import _const as const
from _util import get_sensor

def get_temperature(name, value, max_val):
    sensor_name = const.SENSOR_NAME_TEMPERATURE_NAME.format(name)
    sensor_value = {
        const.SENSOR_NAME_TEMPERATURE_CURRENT: value,
        const.SENSOR_NAME_TEMPERATURE_MAX: max_val
    }
    return get_sensor(sensor_name, sensor_value)

def get_cpu_usage(name, value, max_val):
    sensor_name = const.SENSOR_NAME_CPU_USAGE_NAME.format(name)
    sensor_value = {
        const.SENSOR_NAME_CPU_USAGE_CURRENT: value,
        const.SENSOR_NAME_CPU_USAGE_MAX: max_val
    }
    return get_sensor(sensor_name, sensor_value)   
    
def get_power(name, value, max_val):
    sensor_name = const.SENSOR_NAME_CPU_USAGE_POWER.format(name)
    sensor_value = {
        const.SENSOR_NAME_CPU_USAGE_POWER_CURRENT: value,
        const.SENSOR_NAME_CPU_USAGE_POWER_MAX: max_val
    }
    return get_sensor(sensor_name, sensor_value)   
    
def get_clock(name, value, max_val):
    sensor_name = const.SENSOR_NAME_CPU_CLOCK.format(name)
    sensor_value = {
        const.SENSOR_NAME_CPU_CLOCK_CURRENT: value,
        const.SENSOR_NAME_CPU_CLOCK_MAX: max_val
    }
    return get_sensor(sensor_name, sensor_value)   
    
def get_fan_speed(name, value, max_val):
    sensor_name = const.SENSOR_NAME_CPU_CLOCK.format(name)
    sensor_value = {
        const.SENSOR_NAME_CPU_CLOCK_CURRENT: value,
        const.SENSOR_NAME_CPU_CLOCK_MAX: max_val
    }
    return get_sensor(sensor_name, sensor_value)   
    
from gpiozero import DistanceSensor
import _util as util

sensor = DistanceSensor(24, 23)

def get_closer():
    sensors = []
    sensors.append(util.get_sensor("Distance to Sensors", sensor.distance))

    return sensors
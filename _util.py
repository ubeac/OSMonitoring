
def to_mega_byte(byte_value):
    return int(byte_value / 1048576)

def to_giga_byte(byte_value):
    return int(byte_value / 173741824)

def get_sensor(id, value, type=None, unit=None, prefix=None, dt=None):
    sensor = {
        'id': id,
        'data': value
    }
    return sensor

def secs2hours(secs):
    return round(secs / 3600, 1)

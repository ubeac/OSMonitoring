import _util as util
import _const as const
import speedtest

def get_internet_speed():
    st = speedtest.Speedtest()
    payload = { 
        const.SENSOR_NAME_INTERNET_SPEED_DOWNLOAD : round(st.download()/1000000,2) , 
        const.SENSOR_NAME_INTERNET_SPEED_UPLOAD: round(st.upload()/1000000, 2)
        }
    internet_speed = [util.get_sensor(const.SENSOR_NAME_INTERNET_SPEED_NAME, payload)]

    return internet_speed

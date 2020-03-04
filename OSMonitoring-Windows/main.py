import json 
import threading
import http.client
from disks import get_disks
from memory import get_memory
from battery import get_battery
from net import get_networks
from internet_speed import get_internet_speed
from ohm_sensors import get_ohm_sensors

# Configuration section
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = 'http://myworkspace.hub.ubeac.io/myPC'
DEVICE_FRIENDLY_NAME = 'My Computer'
SENT_INTERVAL = 5 # Sent data interval in second

def main():
    threading.Timer(SENT_INTERVAL, main).start()
    device = [{
        'id': DEVICE_FRIENDLY_NAME,
        'sensors': get_memory() + get_disks() + get_battery() + get_networks() + get_internet_speed() + get_ohm_sensors()
        }]    
    connection = http.client.HTTPSConnection(UBEAC_URL)
    connection.request('POST', GATEWAY_URL, json.dumps(device))
    response = connection.getresponse()
    print(response.read().decode())
       

if __name__ == '__main__':
    main()

    
import json 
import threading
import http.client
from cpu import get_cpus
from disks import get_disks
from memory import get_memory
from battery import get_battery
from fans import get_fans
from net import get_networks
from temperatures import get_temperatures

# Configuration section
UBEAC_URL = 'hub.ubeac.io'
GATEWAY_URL = '/MyComputer'
DEVICE_FRIENDLY_NAME = 'My Computer'
SENT_INTERVAL = 1 # Sent data interval in second

def main():
    threading.Timer(SENT_INTERVAL, main).start()
    device = [{
        'id': DEVICE_FRIENDLY_NAME,
        'sensors': get_memory() + get_disks() + get_cpus() + get_battery() + get_networks() + get_fans() + get_temperatures()
        }]
    
    connection = http.client.HTTPSConnection(UBEAC_URL)
    connection.request('POST', GATEWAY_URL, json.dumps(device))
    response = connection.getresponse()
    print(response.read().decode())
   

if __name__ == '__main__':
    main()
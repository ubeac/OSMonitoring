# OSMonitoring Windows
## Instruction:
* In command prompt run the following commands: 
	- pip install psutil
	- pip install WMI
	- pip install pywin32
	- pip install speedtest-cli
* Download the latest OpenHardwareMonitor and run the executable file to check if the program works with your computer (this program needs to run while you do OS Monitoring)
* Create a gateway (Type: uBeac Generic Gateway Multiple Device)
* Update or get the gateway's URL, your device friendly name, and sent data interval in main.py.
* Run OpenHardwareMonitor executable.
* Run main.py.
* Go to the gateway info page and you should see the live requests. You can click on info icon for each request to see the sensors data.
* Go to the devices page. You should see a device with name: your device friendly name
* Update the details for the sensors (units,...)
* Go to dashboard and drag & drop an indicator. In the setting for the indicator, select the sensor you want to show data.



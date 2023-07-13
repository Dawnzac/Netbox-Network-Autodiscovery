# Netbox-Network-Autodiscovery

### (Undergoing Development)

IP address Autodiscovery and onboarding for Netbox IPAM.

Current functionality only includes running subnet scan and processing output xml file from nmap into a csv file.  
Upload the csv file to your netbox instance.
(DW: Updates are on the way)

```
$ cd netbox-network-autodiscovery
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Configure : 
> network.txt

Includes platform/version Identification. (_**Note: Nmap done on windows will only return hostnames of devices running the same platform(i.e windows)**_)

#### Requirements:
  - Python
  - Nmap
  - NumPy

##### How to Run :
  - run nmap-scan.sh (on Linux)
  - run nmap-scan.bat (on Windows)
      - Then copy the XML files into main folder in linux
      - run python3 netbox-scanner.py nmap in linux

(_**Currently there appear to be some issues with Python code interaction in Windows so, get scan files from Windows and execute it on Linux**_)

(_**Note: Make sure that you are running it inside the same folder/path**_)

Frankensteined from https://github.com/lopes/netbox-scanner/  Thanks @lopes :)

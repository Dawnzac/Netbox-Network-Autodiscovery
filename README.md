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
  - nmap
  - numpy

##### How to Run :
  - run nmap-scan.sh

(_**Note: Make sure that you are running it inside the same folder/path**_)

Frankensteined from https://github.com/lopes/netbox-scanner/  Thanks @lopes :)

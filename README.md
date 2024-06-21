# Netbox-Network-Autodiscovery

### (Undergoing Development)

IP address Autodiscovery and onboarding for Netbox IPAM.

~Current functionality only includes running subnet scan and processing output XML files from Nmap into a CSV file.  
Upload the CSV file to your netbox instance.
(DW: Updates are on the way)~

```
$ cd netbox-network-autodiscovery
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Configure : 
> network.txt

Includes platform/version Identification. (_**Note: Nmap done on Windows will only return hostnames of devices running the same platform(i.e windows)**_)

#### Requirements:
  - Python
  - Nmap
  - NumPy

##### How to Run :
  - run nmap-scan.sh (on Linux)
  - run nmap-scan.bat (on Windows)
      - Then copy the XML files into the main folder in Linux
      - run python3 netbox-scanner.py nmap in Linux

(_**Currently there appear to be some issues with Python code interaction in Windows so, get scan files from Windows and execute it on Linux**_)

**Quick Tip!** :
If you want to transfer files to another system running Linux, try copy via SCP

``` scp -r /path/to/source user@ip:path/to/destination```  
_remove -r if copying a single file_

(_**Note: Make sure that you are running it inside the same folder/path**_)

(_**If there are any issues with installation or working. Install netbox-scanner from the below repo and copy and replace these "__init__.py , nmap-scan.sh and nmap.py" files to main installation**_)


Frankensteined from https://github.com/lopes/netbox-scanner/  Thanks @lopes :)

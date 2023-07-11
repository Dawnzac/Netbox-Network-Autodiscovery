# Netbox-Network-Autodiscovery

### (Undergoing Development)

IP address Autodiscovery and onboarding for Netbox IPAM.

Current functionality only includes processing output xml file from nmap.(DW: Updates are on the way)

#### Configure : 
> network.txt

Includes platform/version Identification. (_**Note: Nmap done on windows will only return hostnames of devices running the same platform(i.e windows)**_)

#### Requirements:
  - Python
  - nmap

##### How to Run :
  - run nmap-scan.sh

(_**Note: Make sure that you are running it inside the same folder/path**_)

Frankensteined from https://github.com/lopes/netbox-scanner/  Thanks @lopes :)

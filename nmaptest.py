import os
import xml.etree.ElementTree as ET
import logging


hosts = list()
unknown = "not found"

def run():
    tree = ET.parse("10.80.30.0.xml")
    root = tree.getroot()

    for host in root.findall('host'):
        try:
            hosts.append((
                host.find('address').attrib['addr'],
                host.find('hostnames').find('hostname').attrib['name'],
                host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                host.find('os').find('osmatch').attrib['name']))
        except AttributeError:
            try:
                hosts.append((
                    host.find('address').attrib['addr'],
                    unknown,
                    host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                    host.find('os').find('osmatch').attrib['name']
                    ))
            except AttributeError:
                try:
                    hosts.append((
                        host.find('address').attrib['addr'],
                        host.find('hostnames').find('hostname').attrib['name'],
                        #host.find('address').attrib['vendor'],
                        unknown,
                        unknown
                        ))
                except AttributeError:
                    hosts.append((
                        host.find('address').attrib['addr'],
                        unknown,
                        #host.find('address').attrib['vendor'],
                        unknown,
                        unknown
                        ))
        #logging.info(f'Address : {host.find("address").attrib["addr"]}')
        #logging.info(f'dns name : {host.find("hostnames").find("hostname").attrib["name"]}')
        #logging.info(f'description : {host.find("os").find("osmatch").find("osclass").attrib["osfamily"]}')
        #logging.info(f'comments : {host.find("os").find("osmatch").attrib["name"]}')
        
if __name__== "__main__":
	run();
	print(*hosts, sep = "\n")

import os
import xml.etree.ElementTree as ET
import logging
import numpy as np

path = os.getcwd()
hosts = list()
unknown = "not found"

def run():
    for f in os.listdir(path):
            if not f.endswith('.xml'):
                continue
            abspath = os.path.join(path, f)
            print(abspath)
            tree = ET.parse(abspath)
            root = tree.getroot()
            for host in root.findall('host'):
                for address in host.iter('address'):
                    logging.debug('for loop inside address')
                    logging.debug({address.get('vendor')})
                    mac = address.get('addr')
                    ven = address.get('vendor')
                    #hosts.append((ipadr,mac,ven))
                try:
                    hosts.append((
                        host.find('address').attrib['addr'],
                        host.find('hostnames').find('hostname').attrib['name'],mac,ven,
                        host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                        host.find('os').find('osmatch').attrib['name']))
                except AttributeError:
                    try:
                        hosts.append((
                            host.find('address').attrib['addr'],
                            ven,mac,ven,
                            host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                            host.find('os').find('osmatch').attrib['name']
                            ))
                    except AttributeError:
                        try:
                            hosts.append((
                                host.find('address').attrib['addr'],
                                host.find('hostnames').find('hostname').attrib['name'],
                                mac,ven,
                                unknown,
                                unknown
                                ))
                        except AttributeError:
                            hosts.append((
                                host.find('address').attrib['addr'],
                                ven,mac,ven,
                                unknown,
                                unknown
                                ))
                #logging.info(f'Address : {host.find("address").attrib["addr"]}')
                #logging.info(f'dns name : {host.find("hostnames").find("hostname").attrib["name"]}')
                #logging.info(f'description : {host.find("os").find("osmatch").find("osclass").attrib["osfamily"]}')
                #logging.info(f'comments : {host.find("os").find("osmatch").attrib["name"]}')
        
if __name__== "__main__":
	run();
	#uncomment below line to see results in cli
	#print(*hosts, sep = "\n")
	np.savetxt("uploadfile.csv", hosts, delimiter=", ", fmt ='% s')

import os
import xml.etree.ElementTree as ET
import logging

class Nmap(object):

    def __init__(self, path, unknown):
        self.unknown = unknown
        self.path = path
        self.hosts = list()

    def run(self):
        for f in os.listdir(self.path):
                if not f.endswith('.xml'):
                    continue
                abspath = os.path.join(self.path, f)
                tree = ET.parse(abspath)
                root = tree.getroot()
                
                for host in root.findall('host'):
                    for address in host.iter('address'):
                        logging.debug('for loop inside address')
                        logging.debug({address.get('vendor')})
                        mac = address.get('addr')
                        ven = address.get('vendor')
                        if ven is None:
                        	ven = "Not-Found"
                        fven= ven.replace(' ','-').replace('(','').replace(')','').replace(',','-').replace('.','-')
                        
                    try:
                        self.hosts.append((
                            host.find('address').attrib['addr'],
                            host.find('hostnames').find('hostname').attrib['name'],mac,ven,
                            host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                            host.find('os').find('osmatch').attrib['name']))
                    except AttributeError:
                        try:
                            self.hosts.append((
                                host.find('address').attrib['addr'],
                                fven,mac,ven,
                                host.find('os').find('osmatch').find('osclass').attrib['osfamily'],
                                host.find('os').find('osmatch').attrib['name']
                                ))
                        except AttributeError:
                            try:
                                self.hosts.append((
                                    host.find('address').attrib['addr'],
                                    host.find('hostnames').find('hostname').attrib['name'],
                                    mac,ven,
                                    self.unknown,
                                    self.unknown
                                    ))
                            except AttributeError:
                                self.hosts.append((
                                    host.find('address').attrib['addr'],
                                    fven,mac,ven,
                                    self.unknown,
                                    self.unknown
                                    ))
                    #logging.info(f'Address : {host.find("address").attrib["addr"]}')
                    #logging.info(f'dns name : {host.find("hostnames").find("hostname").attrib["name"]}')
                    #logging.info(f'description : {host.find("os").find("osmatch").find("osclass").attrib["osfamily"]}')
                    #logging.info(f'comments : {host.find("os").find("osmatch").attrib["name"]}'

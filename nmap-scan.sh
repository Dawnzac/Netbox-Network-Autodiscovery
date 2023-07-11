#!/usr/bin/env bash

#This is just a sample

# mapfile
declare -a NETWORKS
mapfile -t NETWORKS < networks.txt

# small array
#NETWORKS="192.168.3.0/24 192.168.252.0/24"


TODAY="$(date +%d.%m.%yT%H:%M:%S%Z)"

for net in "${NETWORKS[@]}"; do
    NETNAME=$(echo $net | tr -s '/' '-')
    # requires sudo
    #nmap "$net" -T4 -O -F --host-timeout 30s -oX nmap-"$NETNAME".xml
    #nmap "$net" -sU --script nbstat.nse -p137 -oX nmap-"$NETNAME".xml
    # does not require sudo
    nmap "$net" -T4 -O --system-dns --host-timeout 30s -oX nmap-"$NETNAME".xml
    #nmap "$net" -T4 -sn --host-timeout 30s -oX nmap-"$NETNAME".xml
done

python3 nmap.py nmap
tar -czvf scans/nmap-"$TODAY".tar.gz *.xml
rm -rf *.xml

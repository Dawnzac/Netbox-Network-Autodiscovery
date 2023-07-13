@ECHO OFF
CHCP 65001 > NUL


set /A TODAY="$(date+%d.%m.%yT%H:%M:%S%Z)"
echo %TODAY%

FOR /F "usebackq delims="  %%I IN ("networks.txt") DO (
    timeout 3
    echo %%I
    scp D:/netbox/nmap/%%I nbx@10.80.80.80:/home/nbx/Downloads/netbox-scanner/
)
::for net in "${NETWORKS[@]}"; do
::    NETNAME=$(echo $net | tr -s '/' '-')
::    echo $net
    ::nmap "$net" -T4 -O -F --host-timeout 30s -oX nmap-"$NETNAME".xml
    ::nmap "$net" -sU --script nbstat.nse -p137 -oX nmap-"$NETNAME".xml
    ::nmap "$net" -T4 -O --system-dns --host-timeout 30s -oX nmap-"$NETNAME".xml
    ::nmap "$net" -T4 -sn --host-timeout 30s -oX nmap-"$NETNAME".xml
::done


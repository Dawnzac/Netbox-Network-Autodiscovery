@ECHO OFF
CHCP 65001 > NUL

FOR /F "usebackq delims="  %%I IN ("networks.txt") DO (
    timeout 1
    echo %%I
    nmap "%%I" -T4 -O --system-dns --host-timeout 30s -oX nmap-"%%I".xml
)

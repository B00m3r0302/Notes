```
[*] Service scan SMBClient (tcp/139/netbios-ssn/smbclient) ran a command which returned a non-zero exit code (1).
[-] Command: smbclient -L //192.168.196.145 -N -I 192.168.196.145 2>&1
[-] Error Output:


[*] Service scan wkhtmltoimage (tcp/80/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.196.145:80/ /home/kali/Notes/Labs/OSCP-A/192.168.196.145/scans/tcp80/tcp_80_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
[==================>                                         ] 30%
[=====================>                                      ] 35%
[=====================>                                      ] 36%
[======================>                                     ] 37%
[======================>                                     ] 37%
[========================>                                   ] 40%
[========================>                                   ] 40%
[=========================>                                  ] 42%
[==========================>                                 ] 44%
[==========================>                                 ] 44%
qt.network.http2: stream 3 finished with error: "Connection closed"
qt.network.http2: stream 1 finished with error: "Connection closed"
Error: Failed to load https://fonts.googleapis.com/css?family=Montserrat:400,700, with network status code 2 and http status code 0 - Connection closed
Error: Failed to load https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic, with network status code 2 and http status code 0 - Connection closed
[===========================>                                ] 46%
[=============================>                              ] 49%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[==============================>                             ] 50%
[===============================>                            ] 53%
[==================================>                         ] 58%
[=======================================>                    ] 66%
[=============================================>              ] 75%
[=================================================>          ] 83%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::restore: Unbalanced save/restore
QPainter::end: Painter ended with 8 saved states
[============================================================] 100%
Done
Exit with code 1 due to network error: RemoteHostClosedError


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 2>&1
[-] Error Output:


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.1.6.0 2>&1
[-] Error Output:


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.4.2.1.2 2>&1
[-] Error Output:


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.4.2.1.4 2>&1
[-] Error Output:


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.2.3.1.4 2>&1
[-] Error Output:


[*] Service scan SNMPWalk (udp/161/snmp/snmpwalk) ran a command which returned a non-zero exit code (1).
[-] Command: snmpwalk -c public -v 1 192.168.196.145 1.3.6.1.2.1.25.2.3.1.4 2>&1
[-] Error Output:



```
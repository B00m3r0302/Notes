```
[*] Service scan DNS Reverse Lookup (tcp/53/domain/dns-reverse-lookup) ran a command which returned a non-zero exit code (127).
[-] Command: dig -p 53 -x 192.168.145.144 @192.168.145.144
[-] Error Output:
/bin/sh: 1: dig: not found


[*] Service scan DNS Zone Transfer (tcp/53/domain/dns-zone-transfer) ran a command which returned a non-zero exit code (127).
[-] Command: dig AXFR -p 53 @192.168.145.144
[-] Error Output:
/bin/sh: 1: dig: not found


[*] Service scan DNS Reverse Lookup (udp/53/domain/dns-reverse-lookup) ran a command which returned a non-zero exit code (127).
[-] Command: dig -p 53 -x 192.168.145.144 @192.168.145.144
[-] Error Output:
/bin/sh: 1: dig: not found


[*] Service scan DNS Zone Transfer (udp/53/domain/dns-zone-transfer) ran a command which returned a non-zero exit code (127).
[-] Command: dig AXFR -p 53 @192.168.145.144
[-] Error Output:
/bin/sh: 1: dig: not found



```
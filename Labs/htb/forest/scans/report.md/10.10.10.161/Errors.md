```
[*] Service scan DNS Reverse Lookup (tcp/53/domain/dns-reverse-lookup) ran a command which returned a non-zero exit code (9).
[-] Command: dig -p 53 -x 10.10.10.161 @10.10.10.161
[-] Error Output:


[*] Service scan DNS Zone Transfer (tcp/53/domain/dns-zone-transfer) ran a command which returned a non-zero exit code (9).
[-] Command: dig AXFR -p 53 @10.10.10.161
[-] Error Output:


[*] Service scan wkhtmltoimage (tcp/47001/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://10.10.10.161:47001/ /home/kali/Notes/Labs/htb/forest/scans/tcp47001/tcp_47001_http_screenshot.png
[-] Error Output:
Loading page (1/2)
[>                                                           ] 0%
Error: Failed to load http://10.10.10.161:47001/, with network status code 203 and http status code 404 - Error transferring http://10.10.10.161:47001/ - server replied: Not Found
[==============================>                             ] 50%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: ContentNotFoundError



```
```
[*] Service scan SMBClient (tcp/139/netbios-ssn/smbclient) ran a command which returned a non-zero exit code (1).
[-] Command: smbclient -L //192.168.185.141 -N -I 192.168.185.141 2>&1
[-] Error Output:


[*] Service scan wkhtmltoimage (tcp/81/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.185.141:81/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp81/tcp_81_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
[==========================>                                 ] 44%
[===========================>                                ] 45%
[============================>                               ] 47%
[============================>                               ] 47%
[============================>                               ] 48%
[=============================>                              ] 49%
[=============================>                              ] 49%
[==============================>                             ] 50%
Error: Failed to load https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700,300italic,400italic,600italic, with network status code 99 and http status code 0 - Network unreachable
[==============================>                             ] 51%
[======================================>                     ] 64%
[=================================================>          ] 83%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: UnknownNetworkError


[*] Service scan wkhtmltoimage (tcp/80/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.185.141:80/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp80/tcp_80_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
[======>                                                     ] 11%
[=========>                                                  ] 16%
[==============>                                             ] 24%
[================>                                           ] 28%
[===================>                                        ] 32%
[=====================>                                      ] 36%
[========================>                                   ] 41%
[==========================>                                 ] 44%
[===========================>                                ] 46%
[===========================>                                ] 46%
[============================>                               ] 47%
[============================>                               ] 48%
[=============================>                              ] 49%
[=============================>                              ] 49%
** (gst-plugin-scanner:98084): CRITICAL **: 22:09:46.371: _dma_fmt_to_dma_drm_fmts: assertion 'fmt != GST_VIDEO_FORMAT_UNKNOWN' failed
[=============================>                              ] 49%
Error: Failed to load https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i, with network status code 99 and http status code 0 - Network unreachable
Error: Failed to load https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i%7COpen+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i, with network status code 99 and http status code 0 - Network unreachable
[==============================>                             ] 51%
[==================================>                         ] 57%
[==========================================>                 ] 70%
[===============================================>            ] 79%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: UnknownNetworkError


[*] Service scan wkhtmltoimage (tcp/47001/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.185.141:47001/ /home/kali/Notes/Labs/A/192.168.185.141/scans/tcp47001/tcp_47001_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
Error: Failed to load http://192.168.185.141:47001/, with network status code 203 and http status code 404 - Error transferring http://192.168.185.141:47001/ - server replied: Not Found
[==============================>                             ] 50%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: ContentNotFoundError



```
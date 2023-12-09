## File Transfer 
- ftp start
```
ftp <IP>
```
- Start in active mode 
```
ftp <IP> -A
```
- Start active anonymous session
```
ftp <IP> -A -a
```
- switch to active mode
```
quote PASV
```
- switch to passive mode 
```
passive
```
- Set binary encoding 
	- Ensures that files are not modified during the transfer
	- Especially important for images, txt files and executables
```
binary
```
- Upload a file 
```
put <local_file> <output_file>
```
- Download a file
```
get <remote_file> <output_file>
```
- Exit 
```
quit
```
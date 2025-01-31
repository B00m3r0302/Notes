- answered all the questions using gdb and reading the source code 
- Trying to get the point where I get a segmentation fault
- used the following command to find the segmentation fault withing gdb
```
(gdb) run < <(python3 -c 'print("A" * 30)')
```
```
(gdb) run < <(python3 -c 'print("A" * 39)')
```
```
(gdb) run < <(python3 -c 'print("A" * 40)')
```
- Got the segmentation fault at 40
- to find the address of gg in the binary ran the following command in gdb 
```
info address gg
```
- Got the flag
```
HTB{l34rn_th3_b451c5_b3f0r4_u_5t4rt}                            
```
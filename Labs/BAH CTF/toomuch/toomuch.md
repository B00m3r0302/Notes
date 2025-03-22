ELF 64 bit executable 
Buffer size is  20 

| Stack Element      | Size (bytes) |
|--------------------|-------------|
| buffer (char[20]) | 20          |
| Saved RBP         | 8           |
| Return Address    | 8           |

- Total offset to RIP is 20(buffer) + 8 (saved RBP) = 28 bytes
- Need at least 28 bytes to reach RIP and 8 more bytes to overwrite
- Total buffer overflow payload should be at least 36 bytes to take control of execution
# Finding Values
### Find The Address of Win()
```bash
nm toomuch | grep " win"
```
- Output
```
0x4011d5
```
# Exploit
## Notes
- The buffer is 20 bytes because of char buffer[20]
- The saved RBP is 8 bytes
- The return address is the next 8 bytes (which we want to overwrite with win())
## Goals
- Overwrite 20 bytes of buffer
- Overwrite saved RBP (8 bytes of junk)
- Overwrite the retuyrn address (next 8 bytes) with win()

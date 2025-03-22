// Compiled with `gcc -g -fno-stack-protector -no-pie toomuch.c -o toomuch`
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/sendfile.h>
#include <sys/stat.h>
#include <unistd.h>

void setup() {
  setbuf(stdout, 0);
  setbuf(stdin, 0);
  setbuf(stderr, 0);
}

void win() {
  puts("");
  puts("========================");
  puts("*** Winner Winner Chicken Dinner! ***");
  puts("========================");
  puts("");

  sendfile(STDOUT_FILENO, open("./flag.txt", 0), 0, 100);
  fflush(stdout);
}

int main(int argc, char **argv) {

  char buffer[20];

  // Disable buffering
  setup();

  puts("========================");
  puts("*** Welcome to the Buffer Generator! ***");
  puts("========================");

  puts("");
  puts("This is the latest and greatest buffer generator, try making one:");

  printf("Buffer: ");
  scanf("%s", buffer);

  printf("Generating your buffer...\n");
  usleep(500);

  puts("");
  puts("Your custom buffer:");
  puts("========================");

  printf("%s\n", buffer);

  return 0;
}

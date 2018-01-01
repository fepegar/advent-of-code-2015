
#include <stdio.h>
#include <stdbool.h>

int main() {
  int c;
  int floor_number = 0;
  FILE *fp = fopen("input.txt", "r");
  bool basement_found = false;
  int n = 0;
  while ((c = fgetc(fp)) != EOF) {
    if (c == '(')
      floor_number++;
    else if (c == ')') {
      floor_number--;
    }
    n++;
    if (!basement_found && floor_number < 0) {
      printf("First basement: %d\n", n);
      basement_found = true;
    }
  }
  fclose(fp);

  printf("Floor number: %d\n", floor_number);
}


#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 128
#define TRUE 1
#define FALSE 0

int get_floor(char* line);

int main() {
   int floor_number;
   const char* examples_path = "examples1.txt";
   const char* input_path = "input.txt";
   FILE* file;
   char line[256];
   char possible_newline;
   int run_examples = FALSE;

   if (run_examples) {
     // Read examples file
     file = fopen(examples_path, "r");
     if (file != NULL) {
       while (fgets(line, sizeof(line), file)) {
         possible_newline = line[strlen(line) - 1];
         if (possible_newline == '\n') {
           line[strlen(line) - 1] = '\0';  // strip newline
         }
         floor_number = get_floor(line);
         printf("%s: %d\n", line, floor_number);
       }
     }
     fclose(file);
   }

   // Read input file
   floor_number = 0;
   file = fopen(input_path, "r");
   if (file != NULL) {
     while (fgets(line, sizeof(line), file)) {
       possible_newline = line[strlen(line) - 1];
       if (possible_newline == '\n') {
         line[strlen(line) - 1] = '\0';  // strip newline
       }
       floor_number += get_floor(line);
     }
   }
   fclose(file);
   printf("Solution 1: %d\n", floor_number);

   return 0;
}


int get_floor(char* line) {
  int floor_number = 0;
  int length = strlen(line);
  char direction;
  const char UP = '(';
  const char DOWN = ')';

  for (int i = 0; i < length; i++) {
    direction = line[i];
    if (direction == UP) {
      floor_number++;
    } else if (direction == DOWN) {
      floor_number--;
    }
  }
  return floor_number;
}

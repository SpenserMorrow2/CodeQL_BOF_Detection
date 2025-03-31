#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void buf(char *str) {
    char buffer[16]; 

    strncpy(buffer, str, sizeof(buffer) - 1); //safer function, caps # bytes cpyd
    buffer[sizeof(buffer) - 1] = '\0';  

    printf("Buffer content: %s\n", buffer);

}

int main(int argc, char *argv[]) {
    
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    char str[256]; //larger buffer
    fgets(str, sizeof(str), file);
    fclose(file);
    
    buf(str); //call vulnerable func
    printf("Returned Properly\n");
    return 0;
}

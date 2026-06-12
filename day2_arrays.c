#include <stdio.h>

int main() {
    int scores = {10, 20, 30};

    printf("==================================================\n");
    printf("[TRACKING] Hardware Array Memory Layout\n");
    printf("==================================================\n");
    
    // Printing the raw hexadecimal memory addresses using the %p formatter
    printf("Element 0: Value = %d, Address = %p\n", scores, (void*)&scores);
    printf("Element 1: Value = %d, Address = %p\n", scores, (void*)&scores);
    printf("Element 2: Value = %d, Address = %p\n", scores, (void*)&scores);
    
    printf("--------------------------------------------------\n");
    printf("Array Name Pointer Direct Read: %p\n", (void*)scores); 
    // This will match Element 0 perfectly!
    
    return 0;
}
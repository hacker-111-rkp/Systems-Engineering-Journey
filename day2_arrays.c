#include <stdio.h>

int main() {
    // The tells the hardware to allocate 3 sequential slots in RAM
    int scores = {10, 20, 30};

    printf("==================================================\n");
    printf("[TRACKING] Hardware Array Memory Layout\n");
    printf("==================================================\n");
    
    printf("Element 0: Value = %d, Address = %p\n", scores, (void*)&scores);
    printf("Element 1: Value = %d, Address = %p\n", scores, (void*)&scores);
    printf("Element 2: Value = %d, Address = %p\n", scores, (void*)&scores);
    
    printf("--------------------------------------------------\n");
    printf("Array Name Pointer Direct Read: %p\n", (void*)scores); 
    
    return 0;
}
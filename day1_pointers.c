#include <stdio.h>

int main() {
    int core_value = 42;
    int *memory_pointer = &core_value; // '&' fetches the physical RAM address

    printf("==================================================\n");
    printf("[SUCCESS] Day 1 Low-Level Memory Check\n");
    printf("==================================================\n");
    printf("Variable Value: %d\n", core_value);
    printf("Physical RAM Address (Hex): %p\n", (void*)&core_value);
    printf("Pointer Stored Address: %p\n", (void*)memory_pointer);
    printf("Dereferenced Value from RAM: %d\n", *memory_pointer);
    printf("==================================================\n");

    return 0;
}
#include <stdio.h>

int main() {
    int core_value = 42;
    int *memory_pointer = &core_value; // '&' fetches the physical RAM address
    *memory_pointer = 99;
    printf("==================================================\n");
    printf("[SUCCESS] Day 1 Low-Level Memory Check\n");
    printf("==================================================\n");
    printf("Variable Value: %d\n", core_value);
    printf("Physical RAM Address (Hex): %p\n", (void*)&core_value);
    //Give me the exact, physical hexadecimal address of the slot in RAM where 42 is sitting."
    printf("Pointer Stored Address: %p\n", (void*)memory_pointer);
    //*the asterisk tells the compiler: "This variable isn't going to hold a normal number. It is going to hold a raw memory address."
    printf("Dereferenced Value from RAM: %d\n", *memory_pointer);
    //When you use the asterisk * inside your actual logic (not during variable declaration), it means dereference.
    printf("==================================================\n");
    return 0;
}
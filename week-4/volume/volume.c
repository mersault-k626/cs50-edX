// lecture-4.ipynb

// 4.9 Valgrind → 4.9.1 Questions
// 4.15 File I/O
// 4.15.1 RAM versus Persistent Storage
// 4.15.2 The stdio File Functions
// 4.15.3 A Persistent Phone Book
// 4.15.4 Checking fopen
// 4.15.5 Questions
// 4.16 Buffers and a Home-Made cp
// 4.16.1 What "Buffering" Means
// 4.16.2 cp.c: Copying a File Byte by Byte
// 4.16.3 Questions
// 4.18 Cheat Sheet — Week 4 in One Place
// 4.18.1 Operators
// 4.18.2 Functions
// 4.18.3 Memory Map
// 4.18.4 Classic Bugs of Week 4
// section-4.ipynb

// 4.3 Dynamic Memory
// 4.3.1 malloc and free (4.3.1.1 Allocation, 4.3.1.2 Freeing Memory)
// 4.3.2 Common Memory Errors
// 4.4 File I/O
// 4.4.1 fopen and fclose
// 4.4.2 fread and fwrite
// 4.4.3 Copying a File
// 4.4.4 PDF Detection Exercise (closest analog — reads bytes with uint8_t, checks against a header signature)
// 4.4.5 Questions
// shorts-4.ipynb

// 4.4 Dynamic Memory Allocation → 4.4.1 malloc, 4.4.2 free
// 4.6 File Pointers
// 4.6.1 fopen and fclose
// 4.6.2 Single Character I/O
// 4.6.3 Block I/O
// 4.6.4 Questions

// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //  fopen with "w" means fopen will open the file if it exists,
    // write a new one if it doesn't
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // TODO: Read samples from input file and write updated data to output file

    // Close files
    fclose(input);
    fclose(output);
}

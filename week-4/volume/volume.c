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

    // TODO: Copy header from input file to output file, ie the metadata

    // create an array 

    uint8_t header[HEADER_SIZE];

   fread(&header, HEADER_SIZE, 1, input);
   fwrite(&header, HEADER_SIZE, 1, output);


    // read the actual files then copy it to output

    // create buffer for copy
    int16_t buffer;


    // use while loop to copy data from input to buffer

    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // increase the volume using cli input
        buffer *= factor;

        // then write it on the output fil
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}

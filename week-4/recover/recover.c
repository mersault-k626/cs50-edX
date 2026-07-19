#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // check argc (must be exactly 2)
    // if fails, 1
    if (argc != 2)
    {
        printf("Usage: .recover 'user input\n");
        return 1;
    }

    // open argv[1], "r" for read

    FILE *card = fopen(argv[1], "r");

    // create buffer for jpeg's 512-byte block

    uint8_t buffer[512];

    // create counter for jpeg
    int i = 0;

    // create base filename
    char *filename = malloc(16);

    // placeholder for jpeg file
    FILE *img = NULL;

    // loop through argc[1] to write jpegs
    while (fread(buffer, 1, 512, card) == 512)
    {
        // check for jpeg signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // for the first jpeg, create a new file and write to it
            if (i == 0)
            {

                sprintf(filename, "%03i.jpg", i);

                img = fopen(filename, "w");

                fwrite(buffer, 1, 512, img);

                // increment to get to the next jpeg
                i++;
            }
            else
            {
                // close the current jpeg file
                fclose(img);

                // update filename
                sprintf(filename, "%03i.jpg", i++);

                // create and open new file
                img = fopen(filename, "w");

                // assign signature
                fwrite(buffer, 1, 512, img);
            }
        }
        else
        {

            if (img == NULL)
            {
            }
            else
            {

                fwrite(buffer, 1, 512, img);
            }
        }
    }

    // close files and free memory
    fclose(img);
    fclose(card);
    free(filename);
}

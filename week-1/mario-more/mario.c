#include <cs50.h>
#include <stdio.h>

void bricks(int n)
{
    int i = 0; // i = current row
    do
    {
        int j = 0;
        // print leading spaces; guard needed since spaces can be 0 on last row
        if (j < n - 1 - i) do { printf(" "); j++; } while (j < n - 1 - i);
        // print left half bricks (i+1 hashes per row)
        j = 0;
        do { printf("#"); j++; } while (j < i + 1);
        // print gap between left and right pyramids
        printf("  ");
        // print right half bricks (same count as left)
        j = 0;
        do { printf("#"); j++; } while (j < i + 1);
        // end of row
        printf("\n");
        i++; // move to next row
    }
    while (i < n); // stop after n rows
}

int main(void)
{
    int n = 0;
    // keep asking until height is within 1-8
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    bricks(n);
}

// for-only version:
//
// void bricks(int n)
// {
//     for (int i = 0; i < n; i++) // i = current row, runs n times
//     {
//         for (int j = 0; j < n - 1 - i; j++) // leading spaces decrease each row
//             printf(" ");
//         for (int j = 0; j < i + 1; j++) // left bricks increase each row
//             printf("#");
//         printf("  "); // gap between pyramids
//         for (int j = 0; j < i + 1; j++) // right bricks, same count as left
//             printf("#");
//         printf("\n"); // end of row
//     }
// }
//
// int main(void)
// {
//     int n = 0;
//     for (; n < 1 || n > 8;) // keep asking until height is within 1-8
//         n = get_int("Height: ");
//     bricks(n);
// }

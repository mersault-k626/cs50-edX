#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *concat(char *s1, char *s2);

int main(void)
{
    // string s1 = get_string("String 1: ");
    // string s2 = get_string("String 2: ");

    // NO MORE TRAINING WHEELS BITCHES
    char *s1 = get_string("String 1: ");
    char *s2 = get_string("String 2: ");

    char *s3 = concat(s1, s2);

    printf("%s\n", s3);

    //free malloc for s3
    free(s3);

}

char *concat(char *s1, char *s2)
{
    // allocate proper memory for s3
    // + 1 for null terminator for the string-like array

    int len1 = strlen(s1);
    int len2 = strlen(s2);

    char *s3 = malloc(len1 +len2 + 1);

    // concat s1 and s2 by looping

    for (int i = 0; i <= len1; i++)
    {
        s3[i] = s1[i];
    }

    for (int i = 0; i < len2; i++)
    {
        s3[len1 + i] = s2[i];
    }

    s3[len1 + len2] = '\0';

    return s3;
}


import json
import re

markdown_content = """# CS50 Section 4

## 4.1 Hexadecimal Notation

Hexadecimal is a base-16 numbering system, frequently used to represent memory addresses because it compactly maps to binary. It is distinguished from base-10 numbers by the prefix `0x`.

Where base-10 uses the digits 0 through 9, hexadecimal uses sixteen digits: 0 through 9, followed by `A` (10), `B` (11), `C` (12), `D` (13), `E` (14), and `F` (15).

A hexadecimal number represents powers of 16. For example, in the number `0x456`, the rightmost digit represents $16^0$, the next represents $16^1$, and the next $16^2$.

### 4.1.1 Questions

1. Convert `0x0F` to decimal.
2. Why is hexadecimal commonly used for memory addresses?

## 4.2 Pointers

Memory is arranged as a sequence of bytes, each with a unique address. When a variable is declared, the system allocates bytes for it at some address.

### 4.2.1 Pointer Syntax

#### 4.2.1.1 Declaration

A pointer is a variable that stores the memory address of another variable.

```c
int *p = &n;
```

The `&` operator retrieves the address of a variable, so `&n` evaluates to the address of `n` (for example, `0x08`).

The `*` in the declaration specifies that `p` is a pointer to an `int`. 

#### 4.2.1.2 Dereferencing

Later, `*` can be used to **dereference** the pointer, meaning "go to the address stored in the pointer".

```c
*p = 9;
```

This instruction follows `p` to the address it stores and assigns the value `9` to that location.

### 4.2.2 Pointer Practice

Consider the following sequence of instructions:

```c
int a = 28;
int b = 50;
int *c = &a;

*c = 14;
c = &b;
*c = 25;
```

Tracing this chronologically:

1. `a` is allocated (say, at `0x12`) and initialized to `28`.
2. `b` is allocated (at `0x13`) and initialized to `50`.
3. `c` is a pointer allocated (at `0x14`) and stores `&a`, which is `0x12`.
4. `*c = 14;` dereferences `c` (going to `0x12`) and overwrites `a`'s value with `14`.
5. `c = &b;` updates the pointer `c` itself to store the address of `b` (`0x13`).
6. `*c = 25;` dereferences the new address in `c` (going to `0x13`) and overwrites `b`'s value with `25`.

### 4.2.3 Questions

1. What is the difference between `int *p` in a declaration and `*p = 5` in an expression?
2. If `p` stores `0x10`, what does `p` evaluate to? What does `*p` evaluate to?

## 4.3 Dynamic Memory

Dynamic memory allows programs to request memory manually at runtime using `malloc`.

### 4.3.1 malloc and free

#### 4.3.1.1 Allocation

The function `malloc` allocates a requested number of bytes and returns a pointer to the first byte of that block.

```c
int *array = malloc(sizeof(int) * 5);
```

If memory is successfully allocated, `array` holds the address of the first integer in a contiguous block of five integers. Memory can be accessed using pointer arithmetic:

```c
*array = 1;
*(array + 1) = 2;
```

This is entirely equivalent to array bracket syntax (`array[0] = 1; array[1] = 2;`).

When memory is exhausted, `malloc` fails and returns `NULL`. It is critical to check for this failure condition:

```c
if (array == NULL)
{
    return 1;
}
```

#### 4.3.1.2 Freeing Memory

Any memory allocated via `malloc` must eventually be returned to the system by passing its pointer to `free`:

```c
free(array);
```

### 4.3.2 Common Memory Errors

Memory management requires precision. Common pitfalls include:

- Failing to `free` every block of memory that was `malloc`ed (causing a memory leak).
- Failing to `fclose` every file that was `fopen`ed.
- Using more memory than was allocated (buffer overflows or writing past the end of an array).

### 4.3.3 Concatenate Exercise

The `concatenate` function joins two strings together, requiring the allocation of a new block of memory large enough to hold both, plus the null terminator.

```c
char *concat(char *s1, char *s2)
{
    // Get memory for s3
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    char *s3 = malloc(len1 + len2 + 1);

    // Copy over the values from s1 and s2
    for (int i = 0; i < len1; i++)
    {
        s3[i] = s1[i];
    }
    for (int i = 0; i < len2; i++)
    {
        s3[len1 + i] = s2[i];
    }

    s3[len1 + len2] = '\\0';
    return s3;
}
```

This logic requires first measuring both strings, allocating `len1 + len2 + 1` bytes, copying the first string, then copying the second string starting from the offset `len1`. Finally, the null terminator is appended to complete the new string.

### 4.3.4 Debugging Memory Exercise

When memory leaks or invalid accesses occur, `valgrind` is the tool of choice. It runs a program within a simulated environment that tracks every byte of allocated memory, warning if any reads or writes go out of bounds, and reporting any bytes left unfreed when the program exits.

Consider `create.c`, a program meant to create a file whose name is provided as a command-line argument:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for improper usage, otherwise, get filename length
    if (argc != 2)
    {
        printf("Wrong usage: Try ./create [filename]\\n");
        return 1;
    }
    int filename_length = strlen(argv[1]);

    // Create a new block of memory to store filename
    char *filename = malloc(sizeof(char) * (filename_length + 1));

    // Check if malloc failed
    if (filename == NULL)
    {
        printf("Malloc failed.");
        return 1;
    }

    // Copy argv[1] into block of memory for filename
    sprintf(filename, "%s", argv[1]);

    // Open new file under the name stored at filename
    FILE *new_file = fopen(filename, "w");

    // Check if fopen failed
    if (new_file == NULL)
    {
        printf("Could not create file.");
        return 1;
    }

    free(filename);
    fclose(new_file);
}
```

A memory-safe program must check the return values of `malloc` and `fopen`, explicitly `free` dynamically allocated memory, and explicitly `fclose` file pointers.

### 4.3.5 Questions

1. Why does `concat` allocate `len1 + len2 + 1` bytes instead of `len1 + len2`?
2. If `malloc` fails, what value does it return?

## 4.4 File I/O

A `FILE` pointer provides a bridge between a C program and files residing on persistent storage.

### 4.4.1 fopen and fclose

```c
FILE *fopen(const char *pathname, const char *mode);
```

The `fopen` function returns a pointer to a `FILE` structure, allowing the file to be read or written.

Supported `mode` values include:
- `"r"`: read mode.
- `"w"`: write mode.
- `"a"`: append mode.

If the file cannot be opened (e.g., it doesn't exist in read mode), `fopen` returns `NULL`.

### 4.4.2 fread and fwrite

```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(void *ptr, size_t size, size_t nmemb, FILE *stream);
```

These functions read or write blocks of data. The arguments configure what and how much is moved:

- `ptr`: The address in memory where data should be stored (for `fread`) or read from (for `fwrite`).
- `size`: The size in bytes of a single element to be processed.
- `nmemb`: The number of elements to process at once.
- `stream`: The `FILE` pointer returned by `fopen`.

Both functions return the number of items successfully processed, allowing a program to detect when the end of a file is reached.

### 4.4.3 Copying a File

A file can be duplicated byte-by-byte using `fread` and `fwrite` in a loop:

```c
#include <stdio.h>

int main(void)
{
    FILE *input = fopen("in.txt", "r");
    if (input == NULL)
    {
        perror("Failed to open in.txt");
        return 1;
    }

    FILE *output = fopen("out.txt", "w");
    if (output == NULL)
    {
        perror("Failed to open out.txt");
        fclose(input);
        return 1;
    }

    char c;
    while (fread(&c, sizeof(char), 1, input) != 0)
    {
        fwrite(&c, sizeof(char), 1, output);
    }

    fclose(input);
    fclose(output);
}
```

In this implementation, the `while` loop continues executing so long as `fread` manages to read one item of size `char`.

### 4.4.4 PDF Detection Exercise

Files often contain a "magic number", a predictable sequence of bytes at their very beginning that identifies their format. All PDF files, for instance, begin with the four-byte sequence `0x25 0x50 0x44 0x46`.

```c
#include <cs50.h>
#include <stdint.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Check for improper usage
    if (argc != 2)
    {
        printf("Improper usage.\\n");
        return 1;
    }

    // Open PDF with inputted filename
    FILE *pdf = fopen(argv[1], "r");
    if (pdf == NULL)
    {
        printf("File not found.\\n");
        return 1;
    }

    uint8_t buffer[4];
    uint8_t signature[] = {0x25, 0x50, 0x44, 0x46};

    // Read the first 4 bytes into the buffer
    fread(buffer, 1, 4, pdf);
    fclose(pdf);

    // Check the buffer contents against the PDF signature
    for (int i = 0; i < 4; i++)
    {
        if (buffer[i] != signature[i])
        {
            printf("Not a PDF.\\n");
            return 0;
        }
    }
    printf("Likely a PDF!\\n");
    return 0;
}
```

This logic reads a four-byte block from the file into an array, then checks each byte sequentially against the known signature.

### 4.4.5 Questions

1. When copying a file byte-by-byte using `fread`, how does the program know to stop?
2. In the `pdf.c` example, why is the buffer declared as `uint8_t` rather than `int`?

## 4.5 Answers

### 4.1 Answers

**1.** `0x0F` evaluates to 15. The `F` sits in the $16^0$ place, which represents 15 units of 1.

**2.** Hexadecimal compactly maps to binary. Because $16$ is $2^4$, exactly four bits are represented perfectly by a single hexadecimal digit, making memory inspection much cleaner than reading binary out right.

### 4.2 Answers

**1.** In the declaration `int *p`, the asterisk indicates that the variable's type is a pointer to an integer. In the expression `*p = 5`, the asterisk is the dereference operator, which instructs the CPU to visit the address stored inside `p` and manipulate that location.

**2.** `p` evaluates to `0x10`, because that is the value stored inside the variable `p`. `*p` evaluates to the data residing at address `0x10`, because dereferencing goes to the location.

### 4.3 Answers

**1.** The `+ 1` provisions an extra byte of space for the null terminator (`\\0`), which is necessary to mark the end of the new string but is not counted by `strlen`.

**2.** `malloc` returns `NULL` to signal that it could not satisfy the allocation request.

### 4.4 Answers

**1.** `fread` returns the number of items successfully read. When it reaches the end of the file and cannot read any more items, it returns `0`, breaking the condition of the `while` loop.

**2.** The file's signature is defined in precise single bytes. An `int` generally occupies four bytes in memory, so reading into an array of `int`s would pull more data than required and misalign the comparisons. A `uint8_t` explicitly guarantees exactly eight bits (one byte) per element, perfectly matching the file's raw binary representation.
"""

cells = []
in_code_block = False
current_cell_content = []

lines = markdown_content.split('\\n')
for line in lines:
    if line.startswith('```'):
        in_code_block = not in_code_block
    
    # Match any heading from # to ######
    match = re.match(r'^#{1,6}\s+.*', line)
    
    if match and not in_code_block:
        # If there's existing content, save it as a cell
        if current_cell_content:
            content_str = '\\n'.join(current_cell_content).strip()
            if content_str:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [content_str]
                })
        
        # Save the heading as its own cell
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line]
        })
        current_cell_content = []
    else:
        current_cell_content.append(line)

# Add any remaining content
if current_cell_content:
    content_str = '\\n'.join(current_cell_content).strip()
    if content_str:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [content_str]
        })

notebook = {
    "cells": cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(r'c:\Users\Mothma\Documents\edX\CS50\week-4\section-4.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

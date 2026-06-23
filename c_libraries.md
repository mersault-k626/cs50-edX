# C Libraries Cheat Sheet (CS50-friendly)

Covers headers beyond `cs50.h` and `stdio.h` commonly used across CS50, written plainly.

Official (denser) reference: [manual.cs50.io](https://manual.cs50.io/) — CS50's own reference manual, the source of truth if this cheat sheet falls out of date.

A "header" file (`.h`) is a promise list — it tells the compiler "these functions exist somewhere" so they can be used without being written from scratch. `#include`-ing the header unlocks the functions inside it.

---

## `ctype.h` — checking what KIND of character something is

Every function here takes one `char` and answers a yes/no question about it (returns non-zero for "yes", `0` for "no").

| Function | Question it answers | Example |
|---|---|---|
| `isalpha(c)` | Is this a letter (a-z, A-Z)? | `isalpha('x')` → true, `isalpha('5')` → false |
| `isdigit(c)` | Is this a digit (0-9)? | `isdigit('7')` → true |
| `isspace(c)` | Is this whitespace (space, tab, newline)? | `isspace(' ')` → true |
| `isupper(c)` | Is this an uppercase letter? | `isupper('A')` → true |
| `islower(c)` | Is this a lowercase letter? | `islower('a')` → true |
| `ispunct(c)` | Is this punctuation (`.`, `,`, `!`, etc.)? | `ispunct('!')` → true |
| `toupper(c)` | Converts to uppercase (doesn't change non-letters) | `toupper('a')` → `'A'` |
| `tolower(c)` | Converts to lowercase | `tolower('A')` → `'a'` |

**Mental model:** each function is a bouncer checking one specific list — "are you on MY list?" — nothing more.

---

## `math.h` — number-crunching beyond `+ - * /`

| Function | What it does | Example |
|---|---|---|
| `round(x)` | Rounds to the nearest whole number (still returns a `double`) | `round(4.6)` → `5.0` |
| `floor(x)` | Always rounds DOWN | `floor(4.9)` → `4.0` |
| `ceil(x)` | Always rounds UP | `ceil(4.1)` → `5.0` |
| `pow(x, y)` | x raised to the power y | `pow(2, 3)` → `8.0` |
| `sqrt(x)` | Square root | `sqrt(9)` → `3.0` |
| `fabs(x)` | Absolute value, for decimals | `fabs(-3.2)` → `3.2` |

**Note:** compiling by hand (not using `make`) requires explicitly linking this library: `clang program.c -lm -o program`. CS50's `make` handles this automatically.

---

## `string.h` — working with whole strings (not part of `cs50.h`'s `string` type directly, but common later)

| Function | What it does | Example |
|---|---|---|
| `strlen(s)` | Length of a string (not counting the invisible end marker) | `strlen("hi")` → `2` |
| `strcmp(a, b)` | Compares two strings; `0` means equal | `strcmp("cat","cat")` → `0` |
| `strcpy(dest, src)` | Copies one string into another | — |
| `strcat(dest, src)` | Glues `src` onto the end of `dest` | — |

**Note:** a `string` from CS50's `get_string()` works fine with these — under the hood it's the same thing C calls `char *`.

---

## `stdlib.h` — memory & program-level utilities

| Function | What it does | Example |
|---|---|---|
| `malloc(n)` | Reserves `n` bytes of memory, returns a pointer to it | used for arrays/structs whose size isn't known until runtime |
| `free(ptr)` | Releases reserved memory | always paired with `malloc` |
| `exit(code)` | Immediately quits the program | `exit(1)` for "quit due to error" |
| `atoi(s)` | Converts a string of digits into an `int` | `atoi("42")` → `42` |

`malloc`/`free` show up properly once dynamic memory allocation is covered (later weeks).

---

## Quick reference: which header for which task

| Task | Header |
|---|---|
| Check if a character is a letter/digit/space | `ctype.h` |
| Round, square root, power | `math.h` |
| Measure/compare/copy strings manually | `string.h` |
| Reserve memory, quit the program, convert string→int | `stdlib.h` |
| Get input from the user (`get_string`, `get_int`...) | `cs50.h` |
| Print/read formatted text (`printf`, `scanf`) | `stdio.h` |

---

*Living reference — extend as new headers appear in later weeks (e.g. `time.h`).*

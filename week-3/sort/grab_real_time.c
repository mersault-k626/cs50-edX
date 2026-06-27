#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Usage: %s <program> <file1> [file2 ...]\n", argv[0]);
        return 1;
    }

    char *program = argv[1];

    for (int i = 2; i < argc; i++)
    {
        struct timespec start, end;
        clock_gettime(CLOCK_MONOTONIC, &start);

        pid_t pid = fork();
        if (pid == 0)
        {
            int devnull = open("/dev/null", O_WRONLY);
            dup2(devnull, STDOUT_FILENO);
            close(devnull);

            execl(program, program, argv[i], NULL);
            perror("execl failed");
            exit(1);
        }

        int status;
        waitpid(pid, &status, 0);
        clock_gettime(CLOCK_MONOTONIC, &end);

        double elapsed = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
        printf("%-20s %.6f s\n", argv[i], elapsed);
    }

    return 0;
}

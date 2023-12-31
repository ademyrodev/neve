#include <stdio.h>
#include <stdlib.h>

#include "comp.h"
#include "core.h"
#include "err.h"

#define READ_BIN "rb"

static char *readFile(const char *fname) {
    FILE *file = fopen(fname, READ_BIN); 

    if (file == NULL) {
        cliErr("could not open file %s.", fname);    
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    size_t fsize = (size_t)ftell(file);
    rewind(file);

    char *buf = malloc(fsize + 1);
    size_t end = (size_t)fread(buf, sizeof (char), fsize, file);

    if (buf == NULL) {
        cliErr("not enough memory to read %s.", fname);
        return NULL;
    }

    buf[end] = '\0';

    fclose(file);

    return buf;
}

static void compileFile(const char *fname) {
    char *contents = readFile(fname);

    if (contents == NULL) {
        return;
    }

    compile(fname, contents);
    free(contents);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        cliErr("too few arguments; aborting.");
        exit(1);
    } else if (argc == 2) {
        const char *fname = argv[1];
        compileFile(fname);
    }
}

#ifndef TYPE_H
#define TYPE_H

#include <stdbool.h>

typedef enum {
  TYPE_UNKNOWN,
  TYPE_INT,
  TYPE_FLOAT,
  TYPE_BOOL,
  TYPE_NIL
} TypeKind;

typedef struct {
  TypeKind kind;
  const char *name;

  /*
  will expand this whole thing later.
  union {
        
  } as;
  */
} Type;

typedef struct {
  // replace this whole thing with a table once we can
  Type *intType;
  Type *floatType;
  Type *boolType;
  Type *nilType;
} TypeTable;

TypeTable *allocTypeTable();

// future signature: bool getType(char *name, Type *t)
bool getType(TypeTable *table, TypeKind kind, Type *t);

bool typesMatch(Type a, Type b);
bool isTypeKnown(Type t);

Type unknownType();

void freeTypeTable(TypeTable *table);

#endif

#ifndef IR_H
#define IR_H

#include "tok.h"
#include "type.h"

#define NODE_AS_INT(node) ((node)->as.i)
#define NODE_AS_FLOAT(node) ((node)->as.f)
#define NODE_AS_BOOL(node) ((node)->as.b)
#define NODE_AS_NIL(node) ((node)->as.nilLoc)
#define NODE_AS_UNOP(node) ((node)->as.unOp)
#define NODE_AS_BINOP(node) ((node)->as.binOp)

typedef enum {
  NODE_INT,
  NODE_FLOAT,
  NODE_BOOL,
  NODE_NIL,
  NODE_UNOP,
  NODE_BINOP
} NodeType;

typedef enum {
  UNOP_NEG        = 1 << 0,
  UNOP_NOT        = 1 << 1,
  UNOP_IS_ZERO    = 1 << 2,
  UNOP_IS_NEG_ONE = 1 << 3,
  UNOP_IS_NIL     = 1 << 4
} UnOpType;

typedef struct Node Node;

typedef struct {
  long value;
  Loc loc;
} Int;

typedef struct {
  double value;
  Loc loc;
} Float;

typedef struct {
  bool value;
  Loc loc;
} Bool;

typedef struct {
  Tok op;
  UnOpType opType;
  Node *operand;
} UnOp;

typedef struct {
  Node *left;
  Tok op;
  Node *right;
} BinOp;

struct Node {
  union {
    Int i;
    Float f;
    Bool b;
    UnOp unOp;
    BinOp binOp;

    Loc nilLoc;
  } as;

  NodeType type;
  Type valType;
};

Node *newInt(TypeTable *table, long value, Loc loc);
Node *newFloat(TypeTable *table, double value, Loc loc);
Node *newBool(TypeTable *table, bool value, Loc loc);
Node *newNil(TypeTable *table, Loc loc);
Node *newUnOp(TypeTable *table, Tok op, UnOpType type, Node *operand);
Node *newBinOp(TypeTable *table, Node *left, Tok op, Node *right);

void freeNode(Node *node);

// we could keep this function in type.h instead, but that would just create 
// some recursive dependencies.
Type inferType(TypeTable *table, Node *node);

bool checkType(Node *node, TypeKind kind);
bool isNum(Node *node);

Loc getLoc(Node *node);
Loc getFullLoc(Node *node);

#endif


// This represent a record in the only schema of this database
enum Type {STR, INT};

typedef struct Persona {
    char name[20];
    char surname[50];
    char address[100];
    int age;
} Persona;

// This is a node of an index that hold a string, implemented as <key, value>
// to get, from the string/integer the corresponding value Persona
typedef struct Node {
    Type type;
    union{
        int integer;
        char* string;
    } key;
    Persona * val; 
    struct Node * left;
    struct Node * right;
} Node;

// A database hold a set of records and a set of indexes
typedef struct {
    Node * name;
    Node * surname;
    Node * address;
    Node * age;
} Database;

// TODO implement the following methods
// The method return a Persona or NULL 


void insert(Database * database, Persona * persona);
Persona* findByName(Database * database, char * name);
Persona* findBySurname(Database * database, char * surname);
Persona* findByAddress(Database * database, char * address);
Persona* findByAge(Database * database, int age);

//Custom
Node* mkNode(Persona* persona, char* str, int num, Type type);
void destroyDB(Database* database);
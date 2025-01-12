#include "database.h"
#include <stdlib.h>

Node * mkNode(Persona* persona, char* str, int num, Type type){
    Node* res = calloc(1, sizeof(Node));
    res->type = type;
    if(type == INT){
        (res->key).integer = num;
    } else {
        (res->key).str = str;
    }
    res->val = persona;
    return res;
}

void addString(Node* node, Persona* persona, char* str){
    if(node == NULL)    
        return;
    else{
        if(str < (node->key).string){
            if(node->left == NULL){ 
                Node* adder = mkNode(persona, str, 0, Type.STR);
                node->left = adder;
                return;
            } else{                     
                addString(node->left, persona, str);
            }
        } if(str > (node->key).string){
            if(node->right == NULL){
                Node* adder = mkNode(persona, str, 0, Type.STR);
                node->right = adder;
                return;
            } else{
                addString(node->right, persona, str);
            }
        }
    }
}

void addInt(Node* node, Persona* persona, int integer){
    if(node == NULL)    
        return;
    else{
        if(integer < (node->key).integer){
            if(node->left == NULL){ 
                Node* adder = mkNode(persona, NULL, integer, Type.INT);
                node->left = adder;
                return;
            } else{                     
                addInt(node->left, persona, integer);
            }
        } if(integer > (node->key).integer){
            if(node->right == NULL){
                Node* adder = mkNode(persona, NULL, integer, Type.INT);
                node->right = adder;
                return;
            } else{
                addInt(node->right, persona, integer);
            }
        }
    }
}

void insert(Database * database, Persona * persona){
    Node* name = database->name;
    Node* surname = database->surname;
    Node* address = database->address;
    Node* age = database->age;


    addString(name, persona, persona->name);
    addString(surname, persona, persona->surname);
    addString(address, persona, persona->address);
    addInt(age, persona, persona->age);
}

Persona* findByName(Database * database, char * name){
    Node* node = database->name;
    return findStrRec(node, name);
}

Persona* findStrRec(Node* node, char* str){
    if(node == NULL){
        return NULL;
    } else{
        char* nodeString = (node->key).string;
        if(nodeString == str){
            return node->val;
        } if(str < nodeString){
            return findStrRec(node->left, str);
        } if(str > nodeString){
            return findStrRec(node->right, str);
        }
    }
}

Persona* findIntRec(Node* node, int num){
    if(node == NULL){
        return NULL;
    } else{
        char* nodeNum = (node->key).num;
        if(nodeNum == str){
            return node->val;
        } if(str < nodeNum){
            return findIntRec(node->left, num);
        } if(str > nodeNum){
            return findIntRec(node->right, num);
        }
    }
}

Persona* findBySurname(Database * database, char * surname){
    Node* node = database->surname;
    return findStrRec(node, surname);
}
Persona* findByAddress(Database * database, char * address){
    Node* node = database->address;
    return findStrRec(node, address);
}
Persona* findByAge(Database * database, int age){
    Node* node = database->age;
    return findIntRec(node, age);
}

void destroyDB(Database* database){
    recursiveDestroy(database->name, 1);
    recursiveDestroy(database->surname, 0);
    recursiveDestroy(database->address, 0);
    recursiveDestroy(database->age, 0);


}

 recursiveDestroy(Node* node, int freePersona){
    if(node == NULL)
        return NULL;
    else{
        if(node->left != NULL){
            return recursiveDestroy(node->left);
        }
        if(node->right != NULL){
            return recursiveDestroy(node->right);
        } if(freePersona){
            free(node->val);
        } 
        free(node);
    }
}
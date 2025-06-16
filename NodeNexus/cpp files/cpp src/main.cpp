#include "bst.h"
#include <iostream>
#include <random>

int main(){
    BST tree;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(1, 100);

    std::cout << "=== Inserting 15 random numbers. ===";

    for (int i = 0; i < 15; i++){
        int num = dist(gen);

        tree.insert(num);
    }

}
#include "bst.h"
#include <iostream>
#include <iomanip>

BST::BST() : root(nullptr){}

BST::~BST() {
    destroyTree(root);
}

void BST::insert(int key){
    root = insert(root, key);
}

TreeNode* BST::insert(TreeNode* node, int key){

    if (!node) return new TreeNode(key);
    if (key < node->key){
        node->left = insert(node->left, key);
    }
    else if (key > node->key){
        node->right = insert(node->right, key);
    }
    return node;
}

void BST::remove(int key){
    root = remove(root, key);
}

TreeNode* BST::remove(TreeNode* node, int key){

    if (!node) return nullptr;

    if (key < node->key){
        node->left = remove(node->left, key);
    }
    else if (key > node->key){
        node->right = remove(node->right, key);
    }
    else{
        if (!node->left){
            TreeNode* temp = node->right;
            delete node;
            return temp;
        }
        else if (!node->right){
            TreeNode* temp = node->left;
            delete node;
            return temp;
        }
        else{
            TreeNode* temp = findMin(node->right);
            node->key = temp->key;
            node->right = remove(node->right, temp->key);
        }
    }
    return node;
}

TreeNode* BST::findMin(TreeNode* node){
    while (node && node->left){
        node = node->left;
    }
    return node;
}

bool BST::search(int key) const {
    return search(root, key);
}

bool BST::search(TreeNode* node, int key) const {
    if (!node) return false;

    if (key == node->key) return true;
    return key < node->key ? search(node->left, key) : search(node->right, key);
}

void BST::printInOrder() const{
    inOrder(root);
    std::cout << std::endl;
}

void BST::inOrder(TreeNode* node) const{
    if (!node) return;

    inOrder(node->left);
    std::cout << node->key << " ";
    inOrder(node->right);
}

void BST::printTree() const{
    printTree(root, 0);
}

void BST::printTree(TreeNode* node, int depth) const{
    if (!node) return;

    printTree(node->right, depth + 1);
    std::cout << std::setw(4 * depth) << "" << node->key << std::endl;
    printTree(node->left, depth + 1);
}

void BST::destroyTree(TreeNode* node){
    if (!node) return;

    destroyTree(node->left);
    destroyTree(node->right);
    delete node;
}


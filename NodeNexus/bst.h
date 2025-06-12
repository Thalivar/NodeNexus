#pragma once
#include "treenode.h"

class BST {
    public:
        BST();
        ~BST();

        void insert(int key);
        void remove(int key);
        bool search(int key) const;
        void printInOrder() const;
        void printTree() const;

    private:
        TreeNode* root;
        TreeNode* insert(TreeNode* node, int key);
        TreeNode* remove(TreeNode* node, int key);
        TreeNode* findMin(TreeNode* node);

        bool search(TreeNode* node, int key) const;
        void inOrder(TreeNode* node) const;
        void printTree(TreeNode* node, int depth) const;
        void destroyTree(TreeNode* node);
};
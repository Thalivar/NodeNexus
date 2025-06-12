#pragma once

struct TreeNode {

    int key;
    int height;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : key(val), height(1), left(nullptr), right(nullptr) {}

};



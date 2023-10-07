/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int checkBalanced(TreeNode* node, bool& balanced) {
        if (!node) {
            return 0;
        }
        if (!node->left && !node->right){
            return 1;
        }
        int left = checkBalanced(node->right, balanced);
        int right = checkBalanced(node->left, balanced);
        if (abs(left - right) > 1) {
            balanced = false;
        }
        return max(left, right) + 1;
    }
    bool isBalanced(TreeNode* root) {
        bool balanced = true;
        checkBalanced(root, balanced);
        return balanced;
    }
};
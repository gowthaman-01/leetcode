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
    int getDiameter(TreeNode* root, int& res) {
        if (!root) {
            return 0; 
        } 
        if (!root->left && !root->right) {
            return 1;
        }
        int left = getDiameter(root->left, res);
        int right = getDiameter(root->right, res);
        res = max(res, max(right + left, max(left, right))); 
        return max(left, right) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0; 
        getDiameter(root, res); 
        return res; 
    }
};
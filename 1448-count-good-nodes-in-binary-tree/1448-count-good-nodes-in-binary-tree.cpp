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
private: 
    int good = 0;
public:
    void findGoodNodes(TreeNode* node, int n) {
        if (!node) {
            return;
        }
        if (node->val >= n) {
            n = node->val; 
            good++;
        }
        findGoodNodes(node->left, n); 
        findGoodNodes(node->right, n); 
    }
    int goodNodes(TreeNode* root) {
        if (!root) {
            return good; 
        }
        findGoodNodes(root, root->val);
        return good;
    }
};
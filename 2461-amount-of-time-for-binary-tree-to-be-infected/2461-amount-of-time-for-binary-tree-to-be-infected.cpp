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
    TreeNode* fillParentsAndFindStart(TreeNode* node, unordered_map<TreeNode*, TreeNode*>& parents, int start) {
        if (!node->left && !node->right) {
            return node->val == start ? node : nullptr;
        }
        TreeNode *possibleStartLeft = nullptr; TreeNode *possibleStartRight = nullptr;
        if (node->left) {
            possibleStartLeft = fillParentsAndFindStart(node->left, parents, start);
            parents[node->left] = node; 
        }
        if (node->right) {
            possibleStartRight = fillParentsAndFindStart(node->right, parents, start);
            parents[node->right] = node; 
        }
        return node->val == start 
            ? node 
            : possibleStartLeft ? possibleStartLeft : possibleStartRight;
        
    }
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<TreeNode*, TreeNode*> parents; 
        TreeNode* startNode = fillParentsAndFindStart(root, parents, start); 
        queue<TreeNode*> q({startNode});
        unordered_set<int> infected({startNode->val});
        int minutes = -1;       
        while (!q.empty()) {
            minutes++; 
            int length = q.size();
            for (int i = 0; i < length; i++) {
                TreeNode* node = q.front(); 
                q.pop(); 
                if (parents.count(node) && !infected.count(parents[node]->val)) {
                    q.push(parents[node]);
                    infected.insert(parents[node]->val);
                }
                if (node->left && !infected.count(node->left->val)) {
                    q.push(node->left);
                    infected.insert(node->left->val);
                }
                if (node->right && !infected.count(node->right->val)) {
                    q.push(node->right);
                    infected.insert(node->right->val);
                }
            }
        }
        return minutes; 
    }
};
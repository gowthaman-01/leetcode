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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) {
            return {};
        }

        std::queue<TreeNode*> q({root});
        std::vector<std::vector<int>> level_order;

        while (!q.empty()) {
            size_t level_length = q.size();
            std::vector<int> level;
            level.reserve(level_length);

            while (level_length--) {
                TreeNode* front = q.front();
                q.pop();
                
                if (front->left) {
                    q.push(front->left);
                }
                if (front->right) {
                    q.push(front->right);
                }
                level.push_back(front->val);   
            }

            level_order.emplace_back(level);
        }

        return level_order;
    }
};
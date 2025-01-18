class Solution {
private:
    int find(int node, std::vector<int>& parent) { 
        if (node != parent[node]) {
            parent[node] = find(parent[node], parent);
        }
        return parent[node];
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() > n - 1) {
            return false;
        }

        std::vector<int> parent(n);
        std::vector<int> rank(n, 1);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (auto edge: edges) {
            int p1 = find(edge[0], parent);
            int p2 = find(edge[1], parent);

            if (p1 == p2) {
                return false;
            }

            if (rank[p1] > rank[p2]) {
                parent[p2] = parent[p1];
            } else if (rank[p1] < rank[p2]) {
                parent[p1] = parent[p2];
            } else {
                parent[p2] = parent[p1];
                rank[p1]++;
            }

            n--;
        }

        return n == 1;
    }
};
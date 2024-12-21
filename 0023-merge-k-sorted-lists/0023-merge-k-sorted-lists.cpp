class ListNodeCompare {
public:
    bool operator() (const ListNode* l1, const ListNode* l2) const {
        return l1->val >= l2->val;
    }
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::priority_queue<ListNode*, std::vector<ListNode*>, ListNodeCompare> pq;

        for (ListNode* l: lists) {
            if (l) {
                pq.push(l);
            }
        }

        ListNode dummy = ListNode();
        ListNode* cur = &dummy;

        while (!pq.empty()) {
            ListNode* lowest = pq.top();
            pq.pop();

            cur->next = lowest;
            cur = cur->next;

            lowest = lowest->next;
            if (lowest) {
                pq.push(lowest);
            }
        }

        return dummy.next;
    }
};
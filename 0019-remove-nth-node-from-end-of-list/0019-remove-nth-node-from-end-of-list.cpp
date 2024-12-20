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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur = head;
        ListNode* end = head;
        while (n--) {
            end = end->next;
        }

        while (end && end->next) {
            end = end->next;
            cur = cur->next;
        }

        if (!end) {
            return head->next;
        }

        cur->next = cur->next->next;
        return head;
    }
};
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
    ListNode* getMidNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
       
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow->next;
    }

    ListNode* reverse(ListNode* head) {
        ListNode* cur = head;
        ListNode* prev = nullptr;

        while (cur) {
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }

        return prev;
    }

    void reorderList(ListNode* head) {
        ListNode* mid = getMidNode(head);
        ListNode* cur = head;
        ListNode* other = reverse(mid);

        while (cur) {
            ListNode* temp = cur->next;
            cur->next = other;
            cur = other;
            other = temp;
        }
    }
};
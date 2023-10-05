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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if ((!list1 && !list2) || (!list2 && list1)) {
            return list1;
        } 
        if (!list1 && list2) {
            return list2; 
        }

        ListNode *cur = nullptr;
        ListNode *head = nullptr;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                if (!head) {
                    head = list1; 
                    cur = head;
                } else {
                    cur->next = list1;
                    cur = cur->next;
                }
                list1 = list1->next;
            } else {

                if (!head) {
                    head = list2; 
                    cur = head;
                } else {
                    cur->next = list2;
                    cur = cur->next;
                }
                list2 = list2->next;
            }
        }

        while (list1) {
            cur->next = list1; 
            list1 = list1->next;
            cur = cur->next;
        }

        while (list2) {
            cur->next = list2;
            list2 = list2->next;
            cur = cur->next;
        }
        
        return head;
    }
};
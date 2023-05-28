/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *current = head;
    while (current) {
        struct ListNode *next = current->next;

        while (next && current->val == next->val) {
            next = next->next;
        }

        current->next = next;
        current = next;
    }
    return head;
    
}
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *current = head;
    int index = 0;
    while (current) {
        struct ListNode *follow = head;
        int follow_index = 0;
        while (follow != current) {
            follow = follow->next;
            ++follow_index;
        }
        
        if (follow_index < index) {
            return true;
        }
        
        current = current->next;
        ++index;
    }
    return false;
}
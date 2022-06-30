/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int ll_len(struct ListNode* head)
{
    int cnt = 0;
    
    while (head != NULL) {
        head = head->next;
        cnt++;
    }
    
    return cnt;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    int idx = ll_len(head) - n + 1;
    struct ListNode *prev = NULL, *curr = head;
    
    /* Point to the previous node of the targeted node */
    for (int i = 1; i < idx; i++) {
        prev = curr;
        curr = curr->next;
    }
    
    if (prev) {
        prev->next = curr->next;
        free(curr);
    } else {/* delete the last node */
        curr = head->next;
        free(head);
        head = curr;
    }
    
    return head;
}
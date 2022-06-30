/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* arr[100];
    if(list1 == NULL) return list2;
    if(list2 == NULL) return list1;
    int i;
    for(i=0;list1 != NULL && list2 != NULL;++i){
        if(list1->val >= list2->val){
            arr[i] = list2;
            list2 = list2 -> next;
        }
        else{
            arr[i] = list1;
            list1 = list1 -> next;
        }
    }
    while(list2 != NULL){
        arr[i] = list2;
        list2 = list2 -> next;
        ++i;
    }
    while(list1 != NULL){
        arr[i] = list1;
        list1 = list1 -> next;
        ++i;
    }
    for(int j=0;j<i-1;j++){
        arr[j]->next = arr[j+1];
    }
    return arr[0];
}
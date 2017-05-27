'''
write code to remove duplicates from an unsorted linked list
challenge:
if a temporary buffer is not allowed
'''

def deleteDuplicates(head):
    delflag = 1
    flag = 1
    p = head
    while(p != None and p.next != None):
        if p.val != p.next.val:
            flag = 1
            p = p.next
        elif flag < delflag:
            flag += 1;
            p = p.next
        else:
            p.next = p.next.next
    return head

head = 1->1->2->3->3
print deleteDuplicates(head)
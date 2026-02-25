# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Rotate a list by k spots
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #base cases 
        if(head == None):
            return None
        if(head.next == None):
            return head
        if(k == 0):
            return head 
        #rendo la lista circolare
        tail = head
        length = 1
        while(tail.next):
            tail = tail.next
            length += 1
        tail.next = head 

        #ottimizzazione su k, se ci sono k = len lista giri allora si torna al punto di partenza, posso usare il modulo
        
        k = k % length
        #se dopo l'ottimizzazione sono al punto di ritorno posso ritornare la lista di partenza
        new_tail = head 
        steps = length - k - 1
        for _ in range(steps):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None 

        return new_head 




        
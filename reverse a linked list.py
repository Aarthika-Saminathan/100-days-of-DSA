#method 1  two pointer

class ListNode:
    def __init__(self, val=0, next=None):  # Fixed the constructor
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev  # Fixed the typo (changed 'nex' to 'next')
        prev = curr
        curr = next_node

    return prev  # Return the new head of the reversed list

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating Linked List: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Before reversing..")
print_list(head)

head = reverse_list(head)  # Reverse the linked list

print("After reversing")
print_list(head)


#method 2  recursive method




def reverse_list_recursive(head):
    if not head or not head.next:
        return head  # Base case: If list is empty or one node, return it
    
    new_head = reverse_list_recursive(head.next)  # Reverse rest of list
    head.next.next = head  # Make next node point to current
    head.next = None  # Remove old link
    
    return new_head  # Return new head

# Example Usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = reverse_list_recursive(head)
print_list(head)


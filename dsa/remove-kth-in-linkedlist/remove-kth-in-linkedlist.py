# Given a linked list, return the head of the same linked list but with 
# the k-th node removed from the linked list.

# Example 1->2->3->4->5->6, k = 4 returns 1->2->3->4->6

# Solution O(n) Space complexity O(1)

from linkedlist import Node, LinkedList

def remove_kth(ll, k):
    ll.reverse()
    curr = ll.head
    count = 1

    if k == 1:
        ll.head = ll.head.next
        curr = None

    while curr:
        if count == k-1:
            curr.next = curr.next.next
            break

        next = curr.next
        curr = next
        count += 1

    return ll.reverse()


def main():
    arr = [2,3,4,5,6]
    node = Node(1)
    head = node
    next_val = None

    for val in arr:
        next_val = Node(val)
        node.next = next_val
        node = next_val
    

    ll = LinkedList()
    ll.head = head

    ll.print_ll()
    remove_kth(ll, 5)
    remove_kth(ll, 3)
    remove_kth(ll, 4)
    remove_kth(ll, 1)
    ll.print_ll()


if __name__ == '__main__':
    main()


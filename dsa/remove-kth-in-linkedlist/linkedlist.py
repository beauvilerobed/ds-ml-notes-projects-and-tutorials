class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def print_ll(self):
        curr = self.head
        strings = []
        while curr:
            strings.append(str(curr.val))
            next = curr.next
            curr = next
        
        print('->'.join(strings))


def main():
    arr = [1,2,3,4,5,6]
    node = Node(0)
    head = node
    next_val = None

    for val in arr:
        next_val = Node(val)
        node.next = next_val
        node = next_val
    
    ll = LinkedList()
    ll.head = head

    ll.print_ll()
    ll.reverse()
    ll.print_ll()



if __name__ == '__main__':
    main()
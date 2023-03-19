import sys


class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        """Returns True if the Linked List is empty. Otherwise, returns False."""
        return self.head is None  # self.head == None

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def add_node(self, new_data):
        #Add node at the end of the list.
        nNode = SLLNode(new_data)
        if self.head == None:
            self.head = nNode
            return
        else:
            current = self.head

        while current is not None:
            if current.get_next() != None:
                current = current.get_next()
            else:
                break

        current.set_next(nNode)


    def size(self):
        """Traverses the Linked List and returns an integer value representing
        the number of nodes in the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be visited in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:  # While there are still Nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for
        is present in one of the Nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node in the list.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument
        as its self.data variable. Returns nothing.

        The time complexity is O(n) because in the worst case we have to visit
        every Node before we find the one we need to remove.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A Node with that data value is not present."
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        """ Print contents of the list"""
        if self.head is None:
            return "Linked list is empty. Nothing to print."

        current = self.head
        while current is not None:
            print("Node data = ", current.get_data())
            current = current.get_next()

    def deleteDups(self):
        """ Remove duplicates from the list and list the items"""
        current = self.head
        my_set = []
        previous = current

        while current is not None:
            if current.get_data() in my_set:
                print("Found duplicate ",current.get_data())
                previous.set_next(current)
            else:
                my_set.append(current.get_data())
                previous = current
            current = current.get_next()
        print(my_set)

def create_ll(a):
    sll = SLL()
    for val in a:
        sll.add_front(val)
        #sll.add_node(val)
    size = sll.size()
    print("Size of linked list: ", size)

    return sll

def returnKthtoLast(llist, k):
    """ Return Kth to last item from the linked list """
    if llist is None:
        return 0

    index = returnKthtoLast(llist.get_next(), k) + 1
    if index == k :
        print("Kth to last node data = ", llist.get_data())
    print("current index ", index)
    return index

def reverseandClone(node):
    head = SLL()
    while(node != None):
        head.add_front(node.get_data())
        node = node.get_next()

    return head

def isPalindrome(l1, l2):
    while (l1 != None and l2 != None):
        print("list data",l1.get_data(), l2.get_data())
        if(l1.get_data() != l2.get_data()):
            return False
        l1 = l1.get_next()
        l2 = l2.get_next()

    return (l1 == None and l2 == None)

a = sys.stdin.readline().strip().split(' ')

linked_list = SLL()
""" Create linked list """
linked_list = create_ll(a)
print("Size of LL = ", linked_list.size())
linked_list.print_list()

""" Delete duplicates from the linked list """
#linked_list.deleteDups()

""" Return Kth to last item from the linked list scenario """
returnKthtoLast(linked_list.head, 4)

""" check whether the list is a Palindrome or not"""
reverseList = SLL()
reverseList = reverseandClone(linked_list.head)
reverseList.print_list()

result = isPalindrome(linked_list.head, reverseList.head)
print("is it Palindrome list? ", result)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next, self.head = self.head, new_node
        # new_node.next = self.head
        # self.head = newNode 
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        else:# iterate until self.head doesn't have next value.That will be the end.
            new_node = Node(val)
            last_value = self.head
            while last_value.next != None: # we are saying iterate until you find a value of None
                last_value = last_value.next # saying that value with next = None is the last_value
            last_value.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
                
        return self
my_list = SLinkedList()
my_list.head = Node("Monday")

v1 = Node("Tuesday")
my_list.head.next = v1

v2 = Node("Wensday")
v1.next = v2

my_list.add_to_front("Sunday")
my_list.add_to_back("Thursday")
# v3 = my_list.add_to_back("Thursday")
# v2.next = v3

my_list.print_values()
print('*' * 30) # manual way of printing the values
print(my_list.head.next.next.next.next.value)


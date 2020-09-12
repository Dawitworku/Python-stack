Adding a Value to the Front
A common functionality of a list is to be able to add values, so let's add such a method to our class.

Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:

    class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):	# added this line, takes a value
The first thing our method should do is create a node:

	def add_to_front(self, val):
            new_node = SLNode(val)	# create a new instance of our Node class using the given value
This implies we have already created the Node class. We did this in the previous tab, but as a reminder, in a separate class (same file is okay):

    class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None
We want this new node to be the front of our list, but let's not be too hasty. Since the only node we have a reference to in our list is the head, if we replace it right away, we'll lose our reference to the current head, so let's save it before moving forward:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head	# save the current head in a variable
Currently our new node doesn't have a neighbor. Because we're trying to add this new node to the front, we now know its neighbor should be the current head that we just saved:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head	# SET the new node's next TO the list's current head
Finally, we need this new node to be the head of our list:

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node	# SET the list's head TO the node we created in the last step
            return self	                # return self to allow for chaining
Take a moment to compare this functionality to appending a value to the front of an array. Hopefully you can see some of the benefits--no shifting necessary, no matter how many elements we have in our list!

Traversing Through a List
Since this is pretty abstract, it might be helpful to have a function that goes through each node and prints its value. This is a great opportunity to learn how to traverse through a linked list. To iterate through an array, we used a for loop with an index as our iterator. However, since our linked list isn't indexed, we have to come up with a different iterator. We'll use a pointer that will, in a loop, point at each node.

This method won't require any input:

	def print_values(self):
We need to start at the front of our list, so let's create a pointer to our first node:

	def print_values(self):
            runner = self.head	# a pointer to the list's first node
As long as the runner variable is pointing to a node:

	def print_values(self):
            runner = self.head
            while (runner != None):	# iterating while runner is a node and not None
Let's print its value:

	def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)	# print the current node's value
Then, we need to "increment" our runner to the next node, or update the runner so it is pointing to its neighbor:

	def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
        	runner = runner.next 	# set the runner to its neighbor
            return self	                # once the loop is done, return self to allow for chaining
Traversing Through a List and Adding a Value to the End
Let's practice traversing one more time. If we want to add a new node anywhere in our list, it just needs to become a neighbor of an existing node. To become the last node in our list, the list's current last node needs to point to this new node.

This method will require a value to be added:

	def add_to_back(self, val):	# accepts a value
Then we'll want to create a new node with the given value:

	def add_to_back(self, val):
            new_node = SLNode(val)	# create a new instance of our Node class with the given value
Start an iterator at the beginning of the list:

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head	    # set an iterator to start at the front of the list
Because we want to make it to the last node, we'll want to stop on the node who doesn't have a neighbor:

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):	# iterator until the iterator doesn't have a neighbor
Increment the runner to its neighbor (since we just checked to ensure there is, in fact, a neighbor):

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next # increment the runner to the next node in the list
When the loop has finished running, runner will be pointing to the last node. Its next is currently set to None, but we want to make the new node we created at the beginning of this method to be its neighbor:

	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
Consider the edge case where our list is empty. In that case, adding to the front would be the same as adding to the back. Since we've already written that method, let's use it!

	def add_to_back(self, val):
            if self.head == None:	# if the list is empty
                self.add_to_front(val)	# run the add_to_front method
        	return self	# let's make sure the rest of this function doesn't happen if we add to the front
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            return self                 # return self to allow for chaining
Let's test our class!

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!


Once you have a good grasp of this idea of nodes with pointers, you have the building blocks for building some other really neat data structures like binary search trees, tries, graphs, and more. As it's such a critical concept, practice and review the code above so that you are able to re-create the code demonstrated above without looking at the platform. Make sure you feel very comfortable with adding a new node, traversing through the linked list, etc. Once you can create both SList and Node without looking at the codes above, then move on to some of the additional challenges.

Additional Challenges

remove_from_front(self) - remove the first node and return its value
remove_from_back(self) - remove the last node and return its value
remove_val(self, val) - remove the first node with the given value
Consider the following cases:
the node with the given value is the first node
the node with the given value is in the middle of the list
the node with the given value is the last node
insert_at(self, val, n) - insert a node with value val as the nth node in the list
Consider the following cases:
n is 0
n is the length of the list
n is between 0 and the length of the list
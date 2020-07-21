class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next


if __name__ == "__main__":
    print("LinkedList operations")
    
    # head = ListNode(1)
    # aother_elemnent = ListNode(2)
    # head.next = aother_elemnent
    # c = ListNode(3)
    # aother_elemnent.next = c


    # head.next.next.next

    # a = head.next
    # a = a.next
    # a.next


    obj = MyLinkedList()
    index = 0
    val = 10
    obj.addAtHead(val)
    param_1 = obj.get(index)
    print(param_1)
    val = 20
    obj.addAtTail(val)
    param_1 = obj.get(1)
    print(param_1)
    # obj.addAtIndex(index,val)
    obj.deleteAtIndex(0)
    param_1 = obj.get(0)
    print(param_1)
    


"""
    Cycle Detection: Solution 1
"""
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new 
	# node at the beginning 
	def push(self, new_data): 
		new_node = ListNode(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print it 
	# the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data, end =" ") 
			temp = temp.next


	def detectLoop(self): 
		s = set() 
		temp = self.head 
		while (temp): 
		
			# If we have already has 
			# this node in hashmap it 
			# means their is a cycle 
			# (Because you we encountering 
			# the node second time). 
			if (temp in s): 
				return True
	
			# If we are seeing the node for 
			# the first time, insert it in hash 
			s.add(temp) 
	
			temp = temp.next
		
	
		return False
if __name__ == "__main__":
    print("Cycle Detection ")
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(10) 

    # Create a loop for testing 
    llist.head.next.next.next.next = llist.head; 

    if( llist.detectLoop()): 
        print ("Loop found") 
    else : 
        print ("No Loop ") 


"""
    Cycle Detection: Solution 2
"""
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = ListNode(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# Utility function to print it the linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print(temp.data, ) 
			temp = temp.next


	def detectLoop(self): 
		slow_p = self.head 
		fast_p = self.head 
		while(slow_p and fast_p and fast_p.next): 
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p: 
				return

if __name__ == "__main__":
    print("Cycle Detection 2")
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(10) 

    # Create a loop for testing 
    llist.head.next.next.next.next = llist.head 
    if(llist.detectLoop()): 
        print("Found Loop")
    else: 
        print("No Loop")


"""
    Intersection of LinkedList
"""
def getIntesectionNode(head1, head2): 
	
	current1 = head1 
	current2 = head2 
	
	# If one of the head is None 
	if (not current1 or not current2 ): 
		return -1
		
	# Continue until we find intersection node 
	while (current1 and current2 and current1 != current2): 
		current1 = current1.next
		current2 = current2.next
		
		# If we get intersection node 
		if (current1 == current2): 
			return current1.val 
			
		# If one of them reaches end 
		if (not current1): 
			current1 = head2 
		
		if (not current2): 
			current2 = head1 
			
	return current1.val 

if __name__ == "__main__":
    print("Intersection of LinkedList")
    # Mockup List
    head1 = ListNode(10) 

    head2 = ListNode(3) 

    newNode = ListNode(6) 
    head2.next = newNode 

    newNode = ListNode(9) 
    head2.next.next = newNode 

    newNode = ListNode(15) 
    head1.next = newNode 
    head2.next.next.next = newNode 

    newNode = ListNode(30) 
    head1.next.next = newNode 

    head1.next.next.next = None
    print(getIntesectionNode(head1, head2)) 

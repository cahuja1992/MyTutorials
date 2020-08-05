class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head == None:
          self.head = node 
        else:
          ptr = self.head
          while(ptr.next!=None):
            ptr = ptr.next
          ptr.next = node
          
    def search_item(self, val):
        if self.head == None:
          return False
        ptr = self.head
        while(ptr):
          if ptr.data == val:
            return True
          ptr = ptr.next
        return False

if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  
  print(items.search_item('SQL'))

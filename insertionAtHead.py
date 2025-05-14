class node:
    def __init__(self,value):
        self.val = value
        self.next = None
class LinkedList:
    head = None

    def printLinkedList(self):
        temp = self.head
        while temp != None:
            print(temp.val , end=" ")
            temp = temp.next
    def insertionAtTail(self, value):
        if self.head == None:
            self.head = node(value)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node(value)
    
    def insertionAtHead(self,value):
        temp = node(value)
        temp.next = self.head
        self.head = temp


linkedList = LinkedList()
linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)
linkedList.printLinkedList()


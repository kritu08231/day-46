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
        print()
            
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
    
    def insertion(self,value,k):
        if k ==0:
            insertionAtHead(value)
            return
        
        count = 2
        temp = self.head
        while count < k and temp != None:
            count +=1
            temp = temp.next
        if count <k:
            print('k is grater than len')
            return
        rest = temp.next
        temp.next = node(value)
        temp.next.next = rest
    
    def deletion(self,k):
        if k == 1:
            self.head = self.head.next
            return
        count = 2
        temp = self.head
        while count < k and temp != None:
            count +=1
            temp = temp.next
        if count < k:
            print("K is grater than len")
            return
        temp.next = temp.next.next

linkedList = LinkedList()
linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)
linkedList.insertion(5,3)
linkedList.printLinkedList()
linkedList.deletion(3)
linkedList.printLinkedList()


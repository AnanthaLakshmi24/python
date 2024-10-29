class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
     
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)

Node1.next = Node2
Node2.prev = Node1
Node2.next = Node3
Node3.prev = Node2
Node3.next = Node4
Node4.prev = Node3
current = Node1
x=1
Mark=3
newElement=110

while x != Mark-1:
    current = current.next
    x=x+1

lastNode = current.next
NewNode = Node(newElement)

current.next = NewNode
NewNode.prev = current

NewNode.next = lastNode
lastNode.prev = NewNode

while Node1 != None:
    print(Node1.data)
    Node1 = Node1.next

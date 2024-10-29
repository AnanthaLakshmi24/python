class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
Node1= Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
Node5 = Node(50)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node5
Mark=4
x=1
current = Node1
while x != Mark-1:
    current = current.next
    x = x+1
current.next = current.next.next

while Node1 != None:
    print(Node1.data)
    Node1 = Node1.next

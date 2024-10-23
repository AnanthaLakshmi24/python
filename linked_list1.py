class Node:
    def __init__(self,newvalue):
        self.data=newvalue
        self.next=None
head=Node(0)
current=head
l=[10,20,50,70]
for i in l:
    current.next=Node(i)
    current=current.next
current=head.next
while current!=None:
    print(current.data)
    current=current.next

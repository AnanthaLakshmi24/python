#QUEUE
Front,Rare=-1,-1
l=[]
n=5
def Size(Front,Rare):
  return abs(Front-Rare)

def Display(Front,Rare):
  for i in range(Front,Rare):
    print(l[i],end=" ")

def enqueue(element,Front,Rare):
  if Size(Front,Rare) < n:
    l.append(element)
    Rare=Rare+1
    return [Front,Rare]
  else:
    print("Queue is Full")
    return [Front,Rare]

def dequeue(Front,Rare):
  if Size(Front,Rare)>0:
    Front=Front+1
    return [Front,Rare]
  else:
    print("Queue is empty")
    return [Front,Rare]
x=enqueue(100,Front,Rare)
Front,Rare=x[0],x[1]
x=enqueue(200,Front,Rare)
Front,Rare=x[0],x[1]
x=enqueue(300,Front,Rare)
Front,Rare=x[0],x[1]
x=enqueue(400,Front,Rare)
Front,Rare=x[0],x[1]
x=enqueue(500,Front,Rare)
Front,Rare=x[0],x[1]
x=dequeue(Front,Rare)
Front,Rare=x[0],x[1]
print(Size(Front,Rare))
Display(Front,Rare)
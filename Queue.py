class queue:
  def __init__(self):
    self.lst=[]

  def enque(self,ele):
    self.lst.append(ele)
    self.display()

  def deque(self):
    if self.lst==[]:
      print("Queue is empty")
    del(self.lst[0])
    self.display()

  def display(self):
    print(self.lst)


q=queue()
q.enque(10)
q.enque(20)
q.deque()
q.deque()
q.deque()
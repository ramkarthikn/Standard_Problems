class stack:
  def __init__(self):
    self.lst=[]

  def isEmpty(self):
    if self.lst==[]:
      return False
    else:
      return True

  def push(self,ele):
    self.lst.append(ele)
    print("Element is inserted")
    self.display()

  def pop(self):
    if st.isEmpty():
      print("Stack is underflowing")
    else:
      self.lst.pop()
      print("Element is popped")
      self.display()

  def display(self):
    print(self.lst)
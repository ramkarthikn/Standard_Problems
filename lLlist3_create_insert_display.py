class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Llist:
    def __init__(self):
        self.head=None
        
    def create(self,list1):
        self.head=node(list1[0])
        del(list1[0])
        while(len(list1)>0):
            tmp=node(list1[0])
            tmp.next=self.head
            self.head=tmp
            del(list1[0])

    def insert_beg(self,ele):
        tmp=node(ele)
        tmp.next=self.head
        self.head=tmp
        
    def insert_end(self,ele):
        if self.head==None:
            self.head=node(ele)
        else:
            tmp=self.head
            while(tmp.next!=None):
                tmp=tmp.next
            n1=node(ele)
            tmp.next=n1
            
    def display(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.data,end="->")
            tmp=tmp.next
            
l=Llist()
list1=[10,20,30,40]
l.create(list1)
ele=input("Enter an element to insert at begining : ")
l.insert_beg(ele)
l.display()
print()
ele=input("Enter an element to insert at end : ")
l.insert_end(ele)
l.display()
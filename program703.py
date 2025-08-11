class Node:
    def __init__(self, No):
       self.Data = No
       self.next = None
#################################################################

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCount = 0
#################################################################

    def InsertFirst(self, No):
        newn = Node(No)

        if(self.First == None):   # LL is empty
             self.First = newn
        else:                     # LL contains atleast 1 node
            newn.next = self.First        
            self.First = newn

        self.iCount = self.iCount + 1

#################################################################

    def InsertLast(self, No):
        newn = Node(No)

        if(self.First == None):   # LL is empty
            self.First = newn
        else:                     # LL contains atleast 1 node
           temp = self.First

           while(temp.next != None):
               temp = temp.next

               temp.next = newn   


        self.iCount = self.iCount + 1        
#################################################################

    def Display(self):
        temp = self.First

        while(temp != None):
           print(f"| {temp.Data} | -> ", end="")
           temp = temp.next
           
        print("None")   
#################################################################

    def Count(self):
        return self.iCount
#################################################################

    def DeleteFirst(self):
        if(self.First == None):
            return
        else:
            temp = self.First
            self.First = self.First.next
            del temp

            self.iCount = self.iCount - 1    
#################################################################
        
    def DeleteLast(self):
        if(self.First == None):  #LL is empty
            return 
        elif(self.First.next == None):               #n  LL contains 1 node
            del self.First
            self.First = None

        else:              #LL cantains more than 1 node
           temp = self.First

           while(temp.next.next != None):
                temp = temp.next
           del temp.next

           temp.next = None    
        self.iCount = self.iCount - 1   
#################################################################   
    def InsertAtPos(self,No,pos):
        if(pos < 1 or pos > self.iCount+1):
            print("Invalid position")
            return
        
        if(pos == 1):
            self.InsertFirst(No)

        elif(pos == self.iCount+1):
            self.InsertLast(No)

        else:
            newn = Node(No)

            for i in range(1,pos-1,1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount= self.iCount + 1    

        

##################################################################       
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid position")
            return
        
        if(pos == 1):
            self.DeleteFirst()

        elif(pos == self.iCount):
            self.DeleteLast()

        else:
            for i in range(1,pos-1,1):
                temp = temp.next

            target = temp.next    

            temp.next = target.next
            del target

            self.iCount= self.iCount - 1    

        

##################################################################     

def main():
    print("Demonstration of singly Linrear Linear List")

    sobj = SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)


    sobj.InsertLast(151)
    sobj.InsertLast(121)
    sobj.InsertLast(111)

    sobj.Display()

    iRet = sobj.Count()

    print(f"Number of nodes are Linked List : {iRet}")

    sobj.InsertAtPos(105,10)

    sobj.Display()

    sobj.DeleteAtPos(5)
    sobj.Display()
    print(f"Number of nodes are Linked List : {iRet}")
 
if __name__ =="__main__":
    main()    
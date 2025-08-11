# Input Row 5 Col : 4
'''
    *  *  *  *  *
    *  *  *  *  *
    *  *  *  *  *
    *  *  *  *  *
    *  *  *  *  *
'''

def Display(Data):
    iRow = 0
    iCol = 0

    for i in range(1,iRow+1,1):
        for i in range(1,iCol+1,1):
            print("*",end="\t")
        print()
    print()        

    
def main():

   print("Enter number of rows")
   Value1 = int(input())

   print("Enter number of column")
   Value2 = int(input())

   Display(Value1,Value2)

if __name__=="__main__":
    main()    
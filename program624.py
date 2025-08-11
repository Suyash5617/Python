# Input : 721
# OUTPUT : 1 2 7

def DisplayDigit(No):
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        No = No // 10
        print(iDigit)


def main():
   print("Enter number : ")
   Value = int(input())

   DisplayDigit(Value)
          
if __name__ =="__main__":
    main()    

  
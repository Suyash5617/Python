def DisplayFactor(iNo):
   
   print(f"Factors of {iNo} are :")

   for i in range(1,iNo):
       if (iNo % i == 0):
           print(i)
 
def main():
    print("Enter number : ")
    iValue = int(input())
    
    DisplayFactor(iValue)

if __name__=="__main__":
    main()    
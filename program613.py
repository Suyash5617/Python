def Division(No1,No2):
    Ans = 0
    Ans = No1 // No2
    return Ans

def main():
   print("Enter First number ")
   Value1 = int(input())

   print("Enter Second number ")
   Value2 = int(input())


   iRet = Division(Value1,Value2)

   print(f"Division of {Value1} & {Value2} is {iRet}")
          
if __name__ =="__main__":
    main()    

  
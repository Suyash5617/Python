# Input 4
#  4 3 2 1

def Display(iNo):
    for i in range(iNo, 0 ,-1):
        print(i, end='\t')

    print("")    
def main():

   print("Enter Number")
   iValue = int(input())

   Display(iValue)

if __name__=="__main__":
    main()    
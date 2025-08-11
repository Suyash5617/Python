def CountVowel(data):
    iCount = 0

    pattern = "aeiouAEIOU"

    for ch in data:
        if(ch in pattern):
            iCount += 1

    return iCount       
        


 
def main():
    print("Enter starting  : ")
    str = input()

    iRet = CountVowel(str)

    print(f"Frequency vowels in {str} is {iRet}")
   

if __name__=="__main__":
    main()    
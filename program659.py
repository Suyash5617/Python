
def CountNonVowel(data):
    iCount = 0

    pattern = "aeiouAEIOU"
    for ch in data:
        if(ch in pattern):
            iCount += 1
        


 
def main():
    print("Enter starting  : ")
    str = int(input())

    iRet = CountNonVowel(str)

    print(f"frequence of vowel  {str} is {iRet}")
   

if __name__=="__main__":
    main()    
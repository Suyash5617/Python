def StrUpr(data):
    output = ""
    i = 0

    for ch in data:
        if (ch >= 'a' and  ch <= 'z'):
              output = output + (ch - 32) # Error
        else:
            output = output + ch

    return output          

 
def main():
    print("Enter starting  : ")
    str = input()

    strX = StrUpr(str)

    print(f"Updated string is {strX}")
   

if __name__=="__main__":
    main()    
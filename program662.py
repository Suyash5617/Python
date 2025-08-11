def Replace(data):
    iCount = 0

    output = []
    for ch in data:
        if(ch == 'a'):
            output.append('_')   # Error
        else:
            output.append(ch)    

    return output

 
def main():
    print("Enter starting  : ")
    str = input()

    strX = Replace(str)

    print(f"Updated string is {str}")
   

if __name__=="__main__":
    main()    
# Input HELLO
'''
   H E L L O
'''

def Display(Data):
    for ch in Data:
        print(ch, end="\t")
    print()
    
def main():

   print("Enter the Value")
   str = input()

   Display(str)

if __name__=="__main__":
    main()    
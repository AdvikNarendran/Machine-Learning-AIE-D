#Write a function to convert categorical variables to numeric using label encoding. Don’t use 
#any existing functionalities. 

def label(a):
    b=[]
    for i in range(len(a)):
        b.append(i)
    return  b

if __name__=="__main__":
    n=int(input("Enter number of categories\n"))
    a=[]
    for i in range(n):
        print(f"Enter Category {i+1}")
        a.append(input("->"))
    
    b=label(a)

    print("sno.\t Category\tCategory(list)")
    for i in range(len(a)):
        print(f"{i+1}\t  {a[i]}\t\t\t{b[i]}")
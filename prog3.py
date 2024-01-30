#Write a program to find the number of common elements between two lists. The lists contain integers

def common(a,b):
    l1=len(a)
    l2=len(b)
    count=0
    if(l1<l2):#checks for shorter list to traverse
        for i in a:
            if(i in b):
                count+=1
    else:
        for i in b:
            if(i in a):
                count+=1
    
    return count

if __name__ == "__main__":
    l1=[]
    l2=[]
    n1=int(input("Enter length of first list: "))
    for i in range(1,n1+1):
        print(f"enter element {i} of list 1")
        l1.append(input("->"))
    n2=int(input("Enter length of second list: "))
    for i in range(1,n2+1):
        print(f"enter element {i} of list 2")
        l2.append(input("->"))

    print("\nThe number of common elements are ",common(l1,l2))
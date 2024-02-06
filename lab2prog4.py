#Write a function to convert categorical variables to numeric using One-Hot encoding. Don’t 
#use any existing functionalities.

def onehot(mc,sc,o):
    op=[]
    for i in o:
        b=[]
        for j in range(len(i)):
            for k in sc[j]:
                if i[j]==k:
                    b.append(1)
                else:
                    b.append(0)
        op.append(b)
    return op






if __name__=="__main__":
    n1=int(input("Enter number of Main categories\n"))
    mc=[]
    for i in range(n1):
        print(f"enter main category {i+1}")
        mc.append(input("->"))
    
    sc=[]
    for i in mc:
        print(f"enter number of sub categories for {i}")      
        k=int(input())
        b=[]
        for j in range(k):
            b.append(input(f"enter sub category {j+1} for {i} : ").lower())
        sc.append(b)
    
    n2=int(input("Enter number of objects "))
    o=[]
    for i in range(n2):
        d=[]
        for j in mc:
            print(f"enter {j} for object {i+1}: ")
            d.append(input("->").lower())
        o.append(d)

    op = onehot(mc,sc,o)
    print(op)
    print("\t",end="")
    k=0
    for i in mc:
        for j in sc[k]:         
            print(f"{i}_{j}\t",end="")
        k+=1
    print()
    k=1
    for i in op:
        print(f"obj {k}\t\t",end="")
        for j in i:
            print(j,"\t\t",end="")
        print("\n")

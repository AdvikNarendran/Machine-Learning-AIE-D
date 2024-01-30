#Write a program that accepts a matrix as input and returns its transpose.


def transpose(a,r,c):
    b=[]
    for i in range(0,c):
        c=[]
        for j in range(0,r):
            c.append(a[j][i])
        b.append(c)
    return b
if __name__ =="__main__":
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    a=[]
    for i  in range(0,r):
        b=[]
        for j in range(0,c):
            print(f"Enter element {j+1} of row {i+1}")
            b.append(int(input("->")))
        a.append(b)
    print("Original matrix is \n",a)
    print("transposed matrix is \n",transpose(a,r,c))
    
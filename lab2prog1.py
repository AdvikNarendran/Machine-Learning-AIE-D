#input 2 vectors of n dimensions and find eucaladian and manhattan distance

def eucdist(a,b):
    count=0.0
    for i in range(len(a)):
        count+=(a[i]-b[i])**2
    dist=count**(1/2)
    return dist

def mandist(a,b):
    count=0.0
    for i in range(len(a)):
        count+=(a[i]-b[i])
    dist=abs(count)
    return dist

if __name__ == "__main__":
    n=int(input("enter number of dimensions: "))
    a=[]
    b=[]
    for i in range(n):
        print(f"Enter value of dimension {i+1} for first vetor: ")
        a.append(int(input("->")))
    
    for i in range(n):
        print(f"Enter value of dimension {i+1} for second vetor: ")
        b.append(int(input("->")))

    print("Eucaledian distance = ", eucdist(a,b))
    print("Manhattan distance = ", mandist(a,b))
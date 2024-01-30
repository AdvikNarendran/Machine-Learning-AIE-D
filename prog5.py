#input 2 vectors of n dimensions and find equidistance

def checkdist(a,b):
    count=0.0
    for i in range(len(a)):
        count+=(a[i]-b[i])**2
    dist=count**(1/2)
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

    print("Answer = ", checkdist(a,b))

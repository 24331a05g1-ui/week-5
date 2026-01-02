n=int(input("enter integer"))
k=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            k=k+1
    if k>0:
        print("it is not a prime number")
    else:
        print("it is prime number")
else:
    print("it is neither prime nor composite")

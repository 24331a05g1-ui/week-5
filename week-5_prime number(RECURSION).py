def prime (n,i=2):
    if n<=1:
        return 0
    if i== n:
        return 1
    if n%i == 0:
        return 0
    return prime(n,i+1)
num=int(input("enter a number :"))
if prime(num):
    print("it is prime number")
else:
    print("it is not a prime number")

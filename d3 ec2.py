a=int(input())
if a==1:
    print(a,"is neither prime nor not prime number")
for i in range(2,a):
    if(a%i)==0:
        print(a,"is not a prime number")
        break
    else:
        print(a,"is a prime number")
        
        

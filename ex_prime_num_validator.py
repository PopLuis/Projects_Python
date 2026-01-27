##Prime number
prime=int(input("Enter the number: "))
count=0
for i in range(1,prime+1):
    if prime%i==0:
        count+=1

if count==2:
    print("The number is prime!")
else:
    print("The number in not prime!")


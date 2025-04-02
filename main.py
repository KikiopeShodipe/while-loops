#input from user
n=int(input("Enter a number of natural numbers to get sum for:"))
#initialize the sum to 0
sum=0
i=1
#while loop
while i<=n:
    sum+=i
    i+=1
print("The sum of the first ",n," natural numbers is:",sum)
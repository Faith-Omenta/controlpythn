
# Write a function that uses while, if and continue statements
# to print all the even numbers between 0 and 50. 
def while_even():
    m=0
    while m<=50:
        m+=1
        if m%2==0:
            continue
            print(m)

# Write a function that takes an integer argument and prints "Prime" if the number 
# is prime, and "Not prime" if the number is not prime.
def multiple_prime():
   num1=20
   num2=30
   for num in range (num1,num2+1):
      if num==1:
         print(num,"is not a prime number")
      elif num<1:
       for i in range(2,num):
           if (num%i) ==0:
              print(num,"is a not prime number")
              break
       else:
           print(num,"is a prime number")
   else:
       print(num,"is not a prime number")
        

# Write a function that takes a list of integers as input and
# prints the sum of all the even numbers in the list.
def even_sum():
    max=25
    sums = 0
    for i in range(1,max+1):
        if i % 2 == 0 : 
            sums += i
            print(sums)

# Write a function that takes any two integers as input, and prints the sum of all the
# numbers between the two integers (inclusive) that are divisible by 3.
def divisible_by_three(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%3==0:
            sum+=i
            print(sum)
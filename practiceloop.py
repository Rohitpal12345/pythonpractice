# wap to print number using for loop 1 to 10.

#for i in range(1,10):
  #  print(i)

# wap to calculate sum of all number 1 to 10

# sum=0
# for i in range (1,11):
#     sum+=i
# print(sum)

# wap to check even number from 1 to 10

# for i in range(1,11):
#     if i%2==0:
#         print(i,"is even number")

# wap to check all odd number from 1 to 10.
# for i in range (1,11):
#     if i%2!=0:
#         print(i,"is odd number")

# wap to sum of all even number from 1 to 10 .
# sum_even=0
# for i in range(1,11):
#     if i%2==0:
#         sum_even+=i
# print(sum_even)

# wap to sum of all odd number from 1 to 10 .
# sum_odd=0
# for i in range(1,11):
#     if i%2!=0:
#         sum_odd+=i
# print(sum_odd)

# wap to check number is armstrong or not 153.
# num=153
# temp=num
# sum=0

# while num>0:
#     remainder=num%10
#     sum=remainder*remainder*remainder+sum
#     num=num//10

# if temp==sum:
#      print("number is armstrong")
# else:
#         print("number is not armstrong")


# wap to check number is armstrong or not taking by user.
# num=int(input("enter your  number"))
# temp=num
# sum=0
# while num>0:
#     remainder=num%10
#     sum=remainder*remainder*remainder+sum
#     num=num//10
# if temp==sum:
#     print(temp," is armstrong number")
# else:
#     print(temp," is not armstrong number")

# wap to chechk given number is palindrome or not 

# num=555
# temp=num
# reverse=0

# while num>0:
#     remainder=num%10
#     reverse=reverse*10+remainder
#     num=num//10
# if reverse==temp:

#     print("number is palindrome")
# else:
#     print("not palindrome")


# wap to check palindrome take input from user.
# num=int(input("enter a number "))
# temp=num
# reverse=0
# while num>0:
#     remainder=num%10
#     reverse=(reverse*10)+remainder
#     num=num//10
# if temp==reverse:
#     print("number is palindrome")
# else:
#     print("not palindrome")
   
# # wap to print sum of alternate number.
# number = "123445884"
# total = 0
# for i in range(0, len(number), 2):
#     total += int(number[i])
# print(total)


#convert number to string then you can sum of alternate digit in given number

# num="1234456789"  
# sum=0
# for i in range(0,len(num),2):
#     sum+= int(num[i])
#     print(sum)

# wap to print sum of even index of given number

# num="1234456789"
# sum=0
# for i in range (1,len(num),2):
#     sum+= int(num[i])
# print(sum)
    

# wap to print factorial of given number

# num=5
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
#     num=num-1
# print(factorial)


# wap to print factorial of given number
num=5
factorial=1

while num>0:
    factorial=factorial*num
    print(num,"num")
    print(factorial,"factorial")
    num=num-1
print("final factorial",factorial)


  
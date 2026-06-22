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
num=int(input("enter your  number"))
temp=num
sum=0
while num>0:
    remainder=num%10
    sum=remainder*remainder*remainder+sum
    num=num//10
if temp==sum:
    print(temp," is armstrong number")
else:
    print(temp," is not armstrong number")





  
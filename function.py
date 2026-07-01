# write a function to print number from 1 to 10.
# def num():
#     for i in range(0,11):
#         print(i,end=" ")

# num()

# write a function to addition of two number from  to .

# def addition():
#     num1=12
#     num2=67
#     num3=num1+num2
#     print("addition of two given number is->",num3)
# addition()

# wap to subtraction of two number using function.
# def sub():
#     num1=23
#     num2=22
#     num3=num1-num2
#     print("Subtraction of two given number is->",num3)
# sub()
    
# wap to multiplicaton  of two number using function.

# def multiply():
#     num1=54
#     num2=45
#     num3=num1*num2
#     print(num3)
# multiply()

# wap to divison of two number using function.
# def div():
#     num1=50
#     num2=5
#     num3=num1/num2
#     num3=num1//num2
#     print("Divison of two given number is",num3)
# div()

# wap to print fibonacci series using function taking argumrment and return 

# def febonacci(a,b): 
#     print(a,b,end=" ")
#     for i in range(8):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# febonacci(0,1)


# wap to print tribonacci series using function taking argumrment and return.
# def tribonacci(a,b,c):
#     print(a,b,c,end=" ")
#     for i in range(5):
#         d=a+b+c;
#         print(d,end=" ")
#         a=b
#         b=c
#         c=d
# tribonacci(0,0,1)   

#wap to print sum of given number in loop using function

# def sum1(n):
#     add=0
#     for i in range(n):
#      add+=i
#     print("sum of given n number is->",add)
# sum1(11)


# wap to check a number is armstrong or not using function

# def armstrong(n):
#    temp=n
#    sum=0
#    while n>0:
#       remainder=n%10
#       sum=remainder*remainder*remainder+sum
#       n=n//10

#    if temp==sum:
#       print(temp,"is armstrong")
#    else:
#       print(temp,"is not armstrong")
# armstrong(154)

# wap to check a number is palinsdrome or not using function
# 121


# def palindrome(n):
#    temp=n
#    reverse=0
 
#    while n>0:
#       remainder=n%10
#       reverse=reverse*10+remainder
#       n=n//10
#    if reverse==temp:
#       print(temp,"is a palindrome number")
#    else:
#       print(temp,"is not a palindrome number")
      
# palindrome(121)

# wap to check even number and their sum using function

def check_even_sum():
    sum=0
    for i in range(1,11):
        if i%2==0:
            sum+=i
            print(i,"is even number")
    print("sum of all even number is->",sum)
check_even_sum()
      

 
   

    

  



  
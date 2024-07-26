# URL: https://www.geeksforgeeks.org/prime-numbers/
# Q-1 Find the number is prime or not
# If any number is dvisible by 1 or themselves is prime
# 2 and 3 are only consecutive number which are prime
"""
Prime number is defined as natural number greater then 1 and is 
divisble 1 and itself
"""
# Prime number remainder should be zero
import sys

#import pdb;pdb.set_trace()
# Brute Force Mechanism

########### Q-1 Find the number is prime or not ###########
# num = sys.argv[1]
# if int(num) == 1 or int(num) ==2 or int(num) == 3 :
#     print(num + " Prime Number")
# elif int(num) %2 ==0 or int(num) % 3 == 0:
#     print(num + " Not prime number")
# else:
#     print(num + " Is a prime number")


########### Q-2: Find which number is prime out of list ###########
listPrime = [12,3,4,1,9,11,997]
for i in listPrime:
    type(i)
    if i == 1 or i ==2 or i == 3:
        print("%d Is a Prime Number"%i)
    elif i % 2 == 0 or i % 3 == 0:
        print("%d Not a Prime Number"%i)
    else:
        print("%d Is a Prime Number"%i)
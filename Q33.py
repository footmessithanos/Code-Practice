#Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.


t=int(input())
import math
for i in range(t):
    A,B=map(int,input().split())
    a=math.gcd(A,B)
    b=math.lcm(A,B)
    print(a,b)

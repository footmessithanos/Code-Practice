#The code given in the IDE is incorrect - Try and debug this program!!! Given 3 integers - A, B and 
#C - you need to find the difference between the highest and the lowest of the given 3 integers.


t = int(input())
for i in range(t):
    A, B, C = map(int, input().split())
    maximum = max(A,B,C)
    minimum = min(A,B,C)
    D = maximum - minimum
    print(D)
    

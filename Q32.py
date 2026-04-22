#Chef is given three numbers A,B, and C.
#He wants to find whether he can select exactly two numbers out of these such that the product of the selected numbers is negative.


t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A*B<0 or B*C<0 or A*C<0:
        print("YES")
    else:
        print("NO")

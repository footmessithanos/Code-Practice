#You are given the sizes of angles of a simple quadrilateral (in degrees) A, B, C and 
#D, in some order along its perimeter. Determine whether the quadrilateral is cyclic.
#Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 180∘







t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split())
    if A+C==180 and B+D==180:
        print("YES")
    else:
        print("NO")

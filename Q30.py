#In Chefland, a valid phone number consists of 5 digits with no leading zeros. Chef went to a store and purchased N items, where the cost of each item is 
#X. Find whether the total bill is equivalent to a valid phone number.



t=int(input())
for i in range(t):
    N,X=map(int,input().split())
    A=N*X 
    A=str(A)
    B=len(A)
    if B==5:
        print("YES")
    else:
        print("NO")

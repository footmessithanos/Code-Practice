#Chef has A patties and B buns.To make 1 burger, Chef needs 1 patty and 1 bun. Find the maximum number of burgers that Chef can make.



t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    print(min(A,B))

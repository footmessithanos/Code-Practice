#Three numbers A, B and C are the inputs. Write a program to find second largest among them.



t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    a.sort()
    print(a[1])

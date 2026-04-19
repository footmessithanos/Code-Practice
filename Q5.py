#Chef bought N items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.
#1 polybag can contain at most 10 items. What is the minimum number of polybags needed by Chef?





t=int(input())
for i in range(t):
    N=int(input())
    if N%10==0:
        print(N//10)
    else:
        print((N//10)+1)

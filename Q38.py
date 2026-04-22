#Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently, Alice's score is A and Bob's score is 
#B. Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that will be further scored in the match before it ends.


t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    print(7-max(A,B))

#Alice likes numbers which are even, and are a multiple of 7. Bob likes numbers which are odd, and are a multiple of 9.
#If Alice likes A, Alice takes home the number.If Bob likes A, Bob takes home the number. If both Alice and Bob don't like the number, Charlie takes it home.
#Given A, find who takes it home.


t=int(input())
for i in range(t):
    A=int(input())
    if A%2==0 and A%7==0:
        print("Alice")
    elif A%2!=0 and A%9==0:
        print("Bob")
    else:
        print("Charlie")

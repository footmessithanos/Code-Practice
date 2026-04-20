#Chef is taking his baby steps into the world of programming. The very first program he's tasked to write is as follows: "Given two integers 
#A and B print A+B." Unfortunately, Chef makes a typo: his program outputs A×B instead of A+B.
#Given the values of A and 
#B, can you help Chef find the absolute difference between the correct answer and the value his program prints?





def multiply(a, b):
    return(a*b)

def sum(x, y):
    return(x+y)
    
def abs_diff(a,b):
    return abs(a-b)



A, B = map(int, input().split())
C = multiply(A, B)
D = sum(A, B)
E = abs_diff(C, D)
print(E)

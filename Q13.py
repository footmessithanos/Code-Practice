#Write a function named calculatePower that takes two integer, base and exponent respectively, and returns the result of raising base to the power of exponent




def calculate_power(base, exponent):
    return base**exponent
    
    
def main():
    base, exponent = map(int, input().split())
    result = calculate_power(base, exponent)
    print(result)


main()
    

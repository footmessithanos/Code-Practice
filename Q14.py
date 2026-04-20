#Develop a function to compute and return the area of a rectangle, given its length and width



def calculate_area(length, width):
    return length*width
    
    
def main():
    length, width = map(int, input().split())
    area = calculate_area(length, width)
    print(area)


main()

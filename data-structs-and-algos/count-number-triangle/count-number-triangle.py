# Given a list of at least three numbers named sides. 
# Each entry in sides represents the length of a side of a triangle. 
# Write a function possible_triangles to determine the number of possible 
# triangles that can be formed using the given side lengths. 
# In the case that more than three side lengths are given, there may be several 
# possible triangles.

# Note: If there are multiple equal side lengths in the list, we consider them as distinct sides.

# Examples:
# Input: sides = [3, 3, 3] -> 1
#        sides = [3, 3, 3, 3] -> 4
#        sides = [1, 2, 3.5] -> 0

def to_check_to_sides(to_check, triangles):
    # sum of two sides is greater
    # than the third

    if (to_check[0] < to_check[1] + to_check[2]) and\
        (to_check[1] < to_check[0] + to_check[2]) and\
         (to_check[2] < to_check[1] + to_check[0]):
        triangles.append(to_check)
    
    return triangles


def possible_triangles(arr):
    n = len(arr)
    triangles = []

    if n <= 2:
        return triangles

    if n == 3:
        triangles = to_check_to_sides(arr, triangles)
        return triangles 
    
    for i in range(n):
        to_check = None
        if i+2 > n-1:
            start = i
            end = (i+2)%n
            to_check = arr[:end+1]+arr[start:]
        else:
            to_check = arr[i:i+3]
        
        # sum of two sides is greater
        # than the third
        triangles = to_check_to_sides(to_check, triangles)
        
    return triangles

def main():
    arr = [float(val) for val in input().split()]
    triangles = possible_triangles(arr)
    print("triangles ",triangles)
    print(len(triangles))


if __name__ == '__main__':
    main()

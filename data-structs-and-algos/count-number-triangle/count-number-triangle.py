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
#        sides = [1, 2, 3, 4, 5, 6] -> 7

# solution: runtime O(N^2) spacetime complexity O(1)

def possible_triangles(arr):
    n = len(arr)
    arr = sorted(arr)
    count = 0
    
    for i in range(n-1, 2, -1):
        left = 0
        right = i-1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                count += right - left
                right -= 1

            else:
                left += 1

    return count

def main():
    arr = [float(val) for val in input().split()]
    count = possible_triangles(arr)
    print("number of triangles ",count)



if __name__ == '__main__':
    main()

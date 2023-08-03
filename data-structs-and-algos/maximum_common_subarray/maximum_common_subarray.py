# Given two arrays with integers, return the maximum length of a common 
# subarray within both array.

# Example: [1, 3, 5, 6, 7], [2, 4, 3, 5, 6] returns 3 longest common subarray is [3, 5, 6]
# Solution: runtime O(MN) space complexity O(MN)


def max_subarray(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    res = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_val = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr1[i-1] == arr2[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
                max_val = max(max_val, res[i][j])
    return max_val
        
def main():
    arr1 = [1, 3, 5, 6]
    arr2 = [2, 4, 3, 5, 6, 10]

    print(max_subarray(arr1, arr2))



if __name__ == '__main__':
    main()
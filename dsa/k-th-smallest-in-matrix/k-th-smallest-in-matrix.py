# Say you have an n-by-n matrix of elements that are sorted in asc order both in
# the columns and rows of the matrix. Return the k-th smallest element of the matrix.


# Example: A = [[1,4,7],
#.              [3,5,9],
#.              [6,8,11]]
# If k=4 return 5

# Solution runtime O(k^2*logk) space complexity O(k)

from heapq import heappush, heappop

def k_smallest(matrix, k):
    n = len(matrix)
    
    min_heap = []

    for i in range(min(n,k)):
        for j in range(min(n,k)):
            heappush(min_heap, matrix[i][j])

    res = 0
    for _ in range(k):
        res = heappop(min_heap)
    
    return res

def main():
    k = int(input())
    n = int(input())
    matrix = []
    for _ in range(n):
        arr = input().split()
        arr = [float(num) for num in arr]
        if len(arr) == n:
            matrix.append(arr)

    print(k_smallest(matrix, k))

if __name__ == '__main__':
    main()

    



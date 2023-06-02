# Say you have an n-by-n matrix of elements that are sorted in asc order both in
# the columns and rows of the matrix. Return the k-th smallest element of the matrix.


# Example: A = [[1,4,7],
#.              [3,5,9],
#.              [6,8,11]]
# If k=4 return 5

from heapq import heappush, heappop

def k_smallest(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    
    min_heap = []

    for i in range(n):
        for j in range(m):
            heappush(min_heap, matrix[i][j])

    res = 0
    for _ in range(k):
        res = heappop(min_heap)
    
    return res

def main():
    k = int(input())
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        arr = input().split()
        arr = [float(num) for num in arr]
        if len(arr) == m:
            matrix.append(arr)

    print(k_smallest(matrix, k))

if __name__ == '__main__':
    main()

    



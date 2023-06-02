# Given a list of coordinates, write a functions to find the k closest point to the origin. 

# Example: A = [[2,-1], [3,2], [4,1], [-1,-1], [-2,2]] with k=3 should return [[-1,-1], [2,-1], [-2,2]]

# Solution runtime O(n*logk) space complexity O(k)

from heapq import heappush, heappop

def dist(coord):
    return coord[0]**2 + coord[1]**2

def k_closest_points(arr,k):
    min_heap = []
    for nums in arr:
        heappush(min_heap, (dist(nums), nums))

    res = []
    for i in range(k):
        res.append(heappop(min_heap)[1])

    return res


def main():
    k = int(input())
    vals = input().split()
    vals = [float(num) for num in vals]

    if len(vals)%2 == 0:
        idx = int(len(vals)/2)
        coords = [ [float(vals[2*i]), float(vals[2*i+1])] for i in range(idx) ]
        print(k_closest_points(coords,k))

if __name__ == '__main__':
    main()

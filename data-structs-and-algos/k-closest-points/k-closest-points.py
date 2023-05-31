# Given a list of coordinates, write a functions to find the k closest point to the origin. 

# Example: A = [[2,-1], [3,2], [4,1], [-1,-1], [-2,2]] with k=3 should return [[-1,-1], [2,-1], [-2,2]]

import heapq

def dist(coord):
    return coord[0]**2 + coord[1]**2

def k_closest_points(arr,k):
    distances = [(dist(nums), nums) for nums in arr]
    largest_vals = heapq.nsmallest(k,distances)
    return largest_vals

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

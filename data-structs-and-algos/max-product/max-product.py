# Given an integer array, return the max product of any three numbers in
# the array

# Example: A = [1,3,4,5] should return 60; B = -2,-4,5,3] should return 40

# Solution: runtime O(n) space O(1)

import heapq

def max_product(arr):
    three_largest = heapq.nlargest(3,arr)
    two_smallest = heapq.nsmallest(2,arr)

    prod_1 = two_smallest[0]*two_smallest[1]*three_largest[0]
    prod_2 = three_largest[0]*three_largest[1]*three_largest[2]

    return max(prod_1,prod_2)

def main():
    arr1 = (input()).split()
    arr1 = [int(num) for num in arr1]
    print(max_product(arr1))

if __name__ == '__main__':
    main()


# Given an integer array, find the sum of the largest contiguous subarray within the array.

# Example A = [-1, -3, 5, -4, 3, -6, 9, 2] returns 11 since [9,2].

# note: if all the elements are negative, you should return 0

# Solution runtime O(N) space complexity O(1)

def max_subarray(arr):

    n = len(arr)
    max_val = arr[0]
    sum = 0

    for i in range(n):
        sum += arr[i]
        max_val = max(max_val, sum)

        if sum < 0:
            sum = 0

    return max_val

def main():
    vals = [float(val) for val in input().split()]
    print(max_subarray(vals))


if __name__ == '__main__':
    main()


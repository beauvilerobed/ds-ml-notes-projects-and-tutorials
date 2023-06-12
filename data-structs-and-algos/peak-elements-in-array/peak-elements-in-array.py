# Given an array of positive integers, a peak element is greater than its neighbors. Write a function
# to find the index of any peak elements. 

# Example: [3, 5, 2, 4, 1] returns either 1 or 3 because the values of those indexes,5 and 4, are both peak elements.

# Solution: runtime O(log N) space complexity O(1)


def peak_values(arr):
    left = 0
    right = len(arr)-1
    while True:
        mid = (left+right)/2
        right_val = arr[mid+1] if mid+1 < len(arr) else float('-inf')
        left_val = arr[mid+1] if mid-1 >= 0 else float('-inf')

        if left_val < arr[mid] and right_val < arr[mid]:
            return mid
        elif arr[mid] < right_val:
            left = mid + 1
        else:
            right = mid - 1


def main():
    arr = [float(val) for val in input().split()]
    print(peak_values(arr))


if __name__ == '__main__':
    main()
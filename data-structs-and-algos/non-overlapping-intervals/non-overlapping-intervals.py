# Given a list of intervals (i.e. [start time, end time]), determine the smallest number
# of intervals to remove from the list, such that the rest of the intervals do not overlap.
# Intervals can touch such as [1, 3] and [3, 5] but not allowed to overlap (e.g. [1,3]
# [2, 5])

# example: [[1,3], [3,5], [2,4], [6,8]] returns 1 since [2,4] should be removed.

# solution: runtime O(N) space complexity O(1)

def smallest_number(arr):
    n = len(arr)

    if n == 0:
        return 0

    arr = sorted(arr, key=lambda k: (k[0], k[1]))
    count, left, right = 0, 0, 0

    for right in range(1, n):
        if arr[left][1] > arr[right][0]:
            count += 1
        if ((arr[left][1] <= arr[right][0]) or (arr[left][1] >= arr[right][1])):
            left = right
    return count

def main():
    intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    print(smallest_number(intervals))


if __name__ == '__main__':
    main()
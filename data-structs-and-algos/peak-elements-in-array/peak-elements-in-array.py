# Given an array of positive integers, a peak element is greater than its neighbors. Write a function
# to find the index of any peak elements. 

# Example: [3, 5, 2, 4, 1] returns either 1 or 3 because the values of those indexes,5 and 4, are both peak elements.


def peak_values(arr):
    n = len(arr)
    if n < 3:
        return None
    for i in range(1,n-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            return i
    
    return None

def main():
    arr = [int(val) for val in input().split()]
    print(peak_values(arr))


if __name__ == '__main__':
    main()
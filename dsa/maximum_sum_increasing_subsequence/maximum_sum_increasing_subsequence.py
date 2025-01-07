# Given a list of positive integers, return the maximum increasing subsequence sum.

# Example: [3, 2, 5, 7, 6] returns 15 since 3+5+7 = 15

# Solution: runtime O(N^2) Space complexity O(1)

def max_incr_subseq_sum(arr):
    n = len(arr)

    res = arr[0]
    for i in range(1, n):
        prev = arr[i-1]
        temp_sum = prev
        for j in range(i, n):
            curr = arr[j]
            if prev < curr:
                temp_sum += curr
                prev = curr
        
        res = max(res,temp_sum)
    
    return res

def main():
    arr = [22, 3, 2, 5, 7, 6]
    print(max_incr_subseq_sum(arr))

    arr = [3, 2, 5, 7, 6]
    print(max_incr_subseq_sum(arr))

    arr = [2, 5]
    print(max_incr_subseq_sum(arr))
    
    arr = [5]
    print(max_incr_subseq_sum(arr))



if __name__ == '__main__':
    main()


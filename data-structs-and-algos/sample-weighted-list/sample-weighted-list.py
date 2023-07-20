# Given a list of several categories. How do we sample from the list according
# to a particular relative weighting scheme.

# Example: categories [A:5, B:10, C:15, D:20]

# Solution if K is len of categories and N is the sum of weights with N >> K then 
# runtime O(K) space complexity O(K)

import random
import numpy as np

def binarysearch(arr, k):
    lo = 0
    hi = len(arr)-1
    best = 0
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] < k:
            lo = mid+1
        elif arr[mid] > k:
            hi = mid-1
        else:
            best = mid
            break

        if arr[mid] - k > 0:
            best = mid
    return best

def sample(arr, weights):
    n = len(weights)
    cum_weights = [sum(weights[:i]) for i in range(1, n+1)]
    num = random.randint(0,cum_weights[-1])
    idx = binarysearch(cum_weights, num)
    return arr[idx]


def main():
    arr = ['A', 'B', 'C', 'D']
    for i in range(0, 1001, 200):
        weights = [5, 10, 15, i]
        samples = []
        for _ in range(1000):
            samples.append(sample(arr, weights))
        unique, counts = np.unique(samples, return_counts=True)

        print('for  case when i={} we have \n{}\n'.format(i, np.asarray((unique, counts)).T))




if __name__ == '__main__':
    main()

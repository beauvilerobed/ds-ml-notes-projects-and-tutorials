# Given a list of one or more distinct integers, write a function to generate all permutations
# of those integers.

# Example: [2,3,4] --> [[2,3,4], [2,4,3], [3,2,4], [3,4,2], [4,3,2], [4,2,3]]

# solution: runtime O(N!) space complexity O(N*N!)

def perm(arr):
    res = []

    if len(arr) == 1:
        return [arr]

    for i in range(len(arr)):
        for combo in perm(arr[:i]+arr[i+1:]):
            res.append([arr[i]]+combo)

    return res


def main():
    vals = [2,3,4]
    print(perm(vals))


if __name__ == '__main__':
    main()

# Given an integers n and k output a list of all of the combination of k
# numbers chosen from 1 to n.

# Example: n = 3 and k = 2 returns [1,2], [1,3], [2,3]

# runtime and space complexity O(N choose K)


def combinations(n, k):
    def backtrack_helper(n, k, res, combos, start, idx):
        if idx == k:
            return res.append(list(combos))
        
        if (start > n) or (idx >= k):
            return
        
        for i in range(start, n+1):
            combos.append(i)
            backtrack_helper(n, k, res, combos, i+1, idx+1)
            combos.remove(i)

    res = []
    backtrack_helper(n, k, res, [], 1, 0)
    return res

def main():
    n1, k1 = 3, 2
    n2, k2 = 6, 4

    print(combinations(n1,k1))
    print(combinations(n2,k2))



if __name__ == '__main__':
    main()
# Given two strings A and B, write a function to return a list of all the start
# indices within A where the substring A is an anagram of B

# Example: A = 'ababababab' B = 'aab' then you want to return [0, 2, 4, 6]

# solution runtime O(N*M) N size of A M size of B  assuming M << M space complexity O(N)

from collections import Counter

def total_anagram(A, B):
    n = len(A)
    m = len(B)

    if m > n:
        return []

    indxs = []

    dict_str = Counter(B)
    dict_substr = Counter(A[:m])

    if dict_str == dict_substr:
        indxs.append(0)
    
    for i in range(n-m):
        prev, curr = A[i], A[i+m]
        dict_substr[prev] -= 1

        if dict_substr[prev] == 0:
            del dict_substr[prev]
            
        dict_substr[curr] += 1

        if dict_str == dict_substr:
            indxs.append(i+1)

    return indxs

def main():
    A = 'ababababab'
    B = 'aab'

    print(total_anagram(A, B))



if __name__ == '__main__':
    main()


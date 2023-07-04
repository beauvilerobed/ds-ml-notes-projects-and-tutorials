# Given two strings A and B, write a function to return a list of all the start
# indices within A where the substring A is an anagram of B

# Example: A = 'abcdcbac' B = 'abc' then you want to return [0,4,5]

# solution runtime O(N*M) N size of A M size of B  assuming M << M space complexity O(N)

from collections import Counter

def total_anagram(A, B):
    n = len(A)
    m = len(B)

    dict_str = Counter(B)

    indxs = []
    if m > n:
        return []
    
    for i in range(n):
        if i+m <= n:
            substr = A[i:i+m] 
            dict_substr = Counter(substr)
            if dict_substr == dict_str:
                indxs.append(i)

    return indxs

def main():
    A = 'ababababab'
    B = 'aab'

    print(total_anagram(A, B))



if __name__ == '__main__':
    main()


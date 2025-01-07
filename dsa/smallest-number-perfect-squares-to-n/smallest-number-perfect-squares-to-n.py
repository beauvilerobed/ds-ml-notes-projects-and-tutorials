# Given a positive integer n, find the smallest number of perfect 
# squares sum up to n.

# example: n = 7 returns 4 since 7 = 4+1+1+1

# Solution: runtime O(N^2) space complexity O(N)



def smallest_square_sum(n):
    res = [num for num in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, int(i**(.5)+1)):
            res[i] = min(res[i], 1+res[i-j**2])
        
    return res[n]

def main():
    n1 = 7
    n2 = 13

    print(smallest_square_sum(n1))
    print(smallest_square_sum(n2))



if __name__ == '__main__':
    main()
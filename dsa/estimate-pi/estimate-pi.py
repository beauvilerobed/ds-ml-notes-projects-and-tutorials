# estimate pi using monte carlo method

# solution: runtime O(n) space complexity O(1)

import random


def estimate_pi(n):
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()

        if x**2+y**2 <= 1:
            count += 1
    
    return 4*(count)/n

def main():
    n = int(input())

    print(estimate_pi(n))



if __name__ == '__main__':
    main()

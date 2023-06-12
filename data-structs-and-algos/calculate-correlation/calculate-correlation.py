# Given two list X and Y, return their correlation

# solution: runtime O(n) space complexity O(n)

import math

def calc_cov(X,Y):
    n = len(X)
    m = len(Y)
    mean_x = sum(X)/n
    mean_y = sum(Y)/m
    prods = []
    for x,y in zip(X,Y):
        prod = (x-mean_x)*(y-mean_y)
        prods.append(prod)
    
    cov = sum(prods)/n
    return cov

def calc_var(X):
    n = len(X)
    mean = sum(X)/n
    means_from_val = [(val-mean)**2 for val in X]
    variance = math.sqrt(sum(means_from_val)/n)
    return variance


def corr(X,Y):
    covariance = calc_cov(X,Y)
    variance_x = calc_var(X)
    variance_y = calc_var(Y)

    correlation = covariance/(variance_x*variance_y)
    return correlation


def main():
    X = [float(val) for val in input().split()]
    Y = [float(val) for val in input().split()]

    print(corr(X, Y))


if __name__ == '__main__':
    main()
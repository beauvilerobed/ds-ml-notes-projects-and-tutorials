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

def calc_sd(X):
    n = len(X)
    mean = sum(X)/n
    means_from_val = [(val-mean)**2 for val in X]
    variance = sum(means_from_val)/n
    sd = math.sqrt(variance)
    return sd


def corr(X,Y):
    covariance_xy = calc_cov(X,Y)
    sd_x = calc_sd(X)
    sd_y = calc_sd(Y)

    correlation_xy = covariance_xy/(sd_x*sd_y)
    return correlation_xy


def main():
    X = [float(val) for val in input().split()]
    Y = [float(val) for val in input().split()]

    print(corr(X, Y))


if __name__ == '__main__':
    main()
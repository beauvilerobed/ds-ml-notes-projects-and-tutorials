# Given two arrays, write a function to get the intersection of two lists.
# Example: a = [1,2,3,4,5] b = [0,1,3,7] output: [1,3]
# Solution runtime and space complexity: O(len(a)+len(b))

def intersection(a,b):
    a = set(a)
    b = set(b)

    if len(a) < len(b):
        return [num for num in b if num in a ]
    else:
        return [num for num in a if num in b]
    

def main():
    input_a = (input()).split()
    input_b = (input()).split()
    print(intersection(input_a, input_b))
    
if __name__ == '__main__':
    main()
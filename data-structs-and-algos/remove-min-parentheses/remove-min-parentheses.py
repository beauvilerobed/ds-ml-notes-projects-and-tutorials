# Given a string with lowercase letters and left and right parentheses, remove the 
# minimum number of parenthese so the string is valid.

# Example: ")a(b((cd)e(f)g)" --> "ab((cd)e(f)g)"

# Solution runtime: O(N) space complexity O(N)


def parentheses(string):
    letters = [letter for letter in string if letter in "()"]
    n = len(letters)

    if n <= 1:
        return n
    
    parenths = letters[:1]

    for i in range(1,n):
        parenths.append(letters[i])

        if (parenths[-1] == ')') and (parenths[-2] == '('):
            parenths.pop()
            parenths.pop()

    parenths = parenths[::-1]
    res = ''   
    
    for  letter in string:
        if parenths and letter == parenths[-1]:
            parenths.pop()
        else:
            res += letter

    return res


def main():
    example = ")a(b((cd)e(f)g)"
    print(parentheses(example))



if __name__ == '__main__':
    main()

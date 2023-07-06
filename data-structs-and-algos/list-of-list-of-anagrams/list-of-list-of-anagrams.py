# Given an array of strings, return a list of lists where each list contains the strings that are
# anagrams of one another.

# Example: ['abc', 'abd', 'cab', 'bad', 'bca', 'acd'] returns  [['abc', 'bca', 'cab'], [abd, 'bad'], ['acd']]

# Solution: runtime O(NMlogM) where N is length of list and M is max length of string in list 
# space complexity O(NM)


from collections import Counter



def get_anagrams(arr):
    anagrams_dict = {}

    for string in arr:
        anagram_dict = Counter(string)
        anagram_dict = dict(sorted(anagram_dict.items()))
        anagram_key = ''.join('{}{}'.format(k, v) for k, v in anagram_dict.items())

        if not anagram_key in anagrams_dict:
            anagrams_dict[anagram_key] = [string]
        else:
            anagrams_dict[anagram_key].append(string)
        
    res = []
    for k in anagrams_dict:
        res.append(anagrams_dict[k])
    
    return res

def main():
    vals = ['abc', 'abd', 'cab', 'bad', 'bca', 'acd'] 
    print(get_anagrams(vals))



if __name__ == '__main__':
    main()
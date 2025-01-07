# If A is friends with B and B is friends with C then A is friends with C indirectly
# Define a friend group to be a group of indirect and direct groups
# Given an n-by-n adjacency matrix N, where N[i][j] = 1 if i and j are friends and zero otherwise
# write a function to determine how many friend groups exist

# solution: runtime O(M^2) where M is length of columns(friends) and space complexity O(M)
# Example: 0 - 1      4 - 5       8 - 6     should return 3
#                     | \         | /
#                     2  3        7

def dfs(friends, i, N):
    friends.add(i)
    len_friends = len(N[i])

    for j in range(len_friends):
        if N[i][j] == 1 and j not in friends:
            dfs(friends, j, N)
        

def number_of_friend_groups(N):
    num = len(N[0])
    groups = 0
    friends = set()

    for i in range(num):
        if i not in friends:
            dfs(friends, i, N)
            groups += 1

    return groups

def main():
    N = [[0,1,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,0],
         [0,0,0,0,1,0,0,0,0],
         [0,0,1,1,0,1,0,0,0],
         [0,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,1,0]]
    
    print(number_of_friend_groups(N))



if __name__ == '__main__':
    main()
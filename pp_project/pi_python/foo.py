# find shortest word in a list
strs = ["flower","flow","flight"]
shortest_word = min(strs,key=len) #returns flow

import itertools
nums = [-1,0,1,2,-1,-4]
list(itertools.combinations(nums,3))
#combination = n!/r!(n-r)! = 6!/3!(6-3)! = 20
# [(-1, 0, 1), (-1, 0, 2), (-1, 0, -1), (-1, 0, -4), (-1, 1, 2), (-1, 1, -1), (-1, 1, -4), (-1, 2, -1), (-1, 2, -4), (-1, -1, -4), (0, 1, 2), (0, 1, -1), (0, 1, -4), (0, 2, -1), (0, 2, -4), (0, -1, -4), (1, 2, -1), (1, 2, -4), (1, -1, -4), (2, -1, -4)]
nums = [-1,0,1,2]
list(itertools.combinations(nums,3))
# [(-1, 0, 1), (-1, 0, 2), (-1, 1, 2), (0, 1, 2)]


# string slicing
s="siwinski"

# iksniwis 
print(s[::-1]) 

# iiiknssw
print(''.join(sorted(s)))

# siwin
print(s[:5])

# return siwinsk
print(s[:7])
print(s[:-1])


# Determine all substrings 
# ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
s='abcd'
substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
print(substrings)







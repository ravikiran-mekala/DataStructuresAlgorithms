"""
Count Vowels/Consonants
   Explanation: Iterate & classify letters.
   Example: hello → v=2, c=3
"""

def count_v_c(s):
    vowels = {'a','e','i','o','u'}
    vc, cc = 0, 0
    for i in s:
        if i in vowels:
            vc += 1
        else:
            cc += 1
    return vc, cc

print(count_v_c("qwerer"))

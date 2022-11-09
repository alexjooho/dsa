class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a dictionary for each string with the frequency of letters
        # Then compare the two dictionaries to see if they are the same

        s_hash = {}
        t_hash = {}

        for char in s:
            s_hash[char] = s_hash.get(char, 0) + 1
        
        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1

        return s_hash == t_hash
        
# somewhat cheating solution:
# return collections.Counter(s) == collections.Counter(t)


# neetcode solution:
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT

# don't need to do "for i in range(len(s))" because it just makes it more work

# could also sort them and compare them, but this has a higher O
# return sorted(s) == sorted(t)

#note: sorted() is a function that returns a new sorted list, list.sort() is a method that sorts in place
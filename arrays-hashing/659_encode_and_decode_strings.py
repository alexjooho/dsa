# Neetcode solution since mine didn't work for edge cases where delimiter was inside of word
# O(n) time complexity

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # e.g. ['neet', 'code'] -> '4#neet4#code'
        return res
    # encode function is technically O(n^2) because string concatenation copies the entire string
    # so the result string is being copied over and over n times
    
    # to make it O(n), we can use a list to mock a string builder
    
    # def encode(self, strs):
    #     return ''.join(f'{len(string)}#{string}' for string in strs)
    
    # this makes a generator of the encoded strings (could put brackets around the comprehension here)
    
    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                # keep going until we find the first "#" character and use the number before it
                # to get the length of the string
                # need to do it like this in case the string length is > double digit value (e.g. length = 20)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            # append the string to the list
            i = j + 1 + length
            # update i
        return res



# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """
#     def encode(self, strs):
#         # write your code here
#         # join the list of strings with # in between

#         return '#'.join(strs)

#     """
#     @param: str: A string
#     @return: dcodes a single string to a list of strings
#     """
#     def decode(self, str):
#         # write your code here
#         # keep a current value that starts as an empty string
#         # keep adding to it until you reach the end of the string or a "#" that is not followed by another "#"
#         # and append it to the list

#         # edge case: a string with # inside of it
#         # e.g. C###jack#apple#

#         output = []
#         current = ''

#         i = 0

#         while i < len(str):
#             if str[i] == '#' and i < len(str) - 1:
#                 # i < len(str) - 1 is so that if # is at the end of the string
#                 # it will not go past the last index of string
#                 if str[i+1] != '#':
#                     output.append(current)
#                     current = str[i+1]
#                     i += 2
                
#                 else:
#                     current += '#'
#                     j = i + 2
#                     while str[j] == '#' and j < len(str):
#                         current += '#'
#                         j += 1
#                     output.append(current)
#                     if j < len(str):
#                         current = str[j]
#                     i = j + 1
            
#             else:
#                 current += str[i]
#                 i += 1
        
#         output.append(current)
#         return output
    
#     # did a while loop since I wanted to check to make sure the next item wasn't also a "#" without
#     # re-iterating over the same indexes (since python doesn't let you add to i during a range loop)
#     # therefore I had to add to i in each case scenario
    
#     # if the next value was also a "#", I added a "#" to account for the current one and then 
#     # skipped the next value (line 41: j = i + 2) so that one "#" would be skipped to account
#     # for the last one being part of the encoding
    
#     # have to do a final output.append(current) since the last word will not have a "#" at the end
    
#     #NOTE: THIS SOLUTION DOESN'T WORK! DOESN'T ACCOUNT FOR EDGE CASES WHERE # IS IN THE MIDDLE OF THE WORD
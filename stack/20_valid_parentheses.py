class Solution:
    def isValid(self, s: str) -> bool:

        # create a stack of opening brackets
        # loop through array, and if there's an opening bracket, add to stack
        # if there is a closing bracket, pop off the stack and make sure it's a valid pair
        # check to make sure the stack has a length > 0 before doing above

        opening_brackets = []
        valid_pairs = {'{}', '()', '[]'}
        closing_brackets = {'}', ')', ']'}

        for bracket in s:
            if bracket in closing_brackets:
                if len(opening_brackets) == 0 or opening_brackets.pop() + bracket not in valid_pairs:
                    return False
            else:
                opening_brackets.append(bracket)

        if len(opening_brackets) > 0:
            return False
        return True

# instead could have just used a dictionary that has the closing bracket as keys, and opening bracket as values
# and then return not stack instead of having to do another if statement

# class Solution:
#     def isValid(self, s: str) -> bool:
#         Map = {")": "(", "]": "[", "}": "{"}
#         stack = []

#         for c in s:
#             if c not in Map:
#                 stack.append(c)
#                 continue
#             if not stack or stack[-1] != Map[c]:
#                 return False
#             stack.pop()

#         return not stack
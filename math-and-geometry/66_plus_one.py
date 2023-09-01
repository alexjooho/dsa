class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start from last index and go backwards, updating digits
        # if digit is not a 9, simply increment it and finish
        # if digit is a 9, change it to 0 and increment the digit in front of it
        # if there is not digit in front, insert a 1 at the front

        i = len(digits) - 1

        while i >= 0:
            cur = digits [i]
            if cur != 9:
                # if the digit is not a 9, we can simply increment and stop
                digits[i] = digits[i] + 1
                break
            elif i == 0:
                # if the digit is a 9 and we are at the beginning of the number
                # we change it to a 0 and insert a 1 at the front
                digits[i] = 0
                digits.insert(0, 1)
                break
            else:
                # if the digit is a 9 and we are not at the beginning
                # we change it to a 0 and decrement i by one
                digits[i] = 0
                i -= 1

        return digits
    
# neetcode solution:
# he simply does it backwards by slicing and reversing the list

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]

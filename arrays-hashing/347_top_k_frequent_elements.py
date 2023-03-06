class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary for the count of each integer
        # create a list with k indexes that all equal 0
        # get the items from the dictionary and sort by their values
        # add to new list

        counter = {}

        k_list = [0] * k

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        sorted_counter = [key for key, value in sorted(counter.items(), key = lambda x: x[1], reverse = True)]

        for i in range(len(k_list)):
            k_list[i] = sorted_counter[i]

        return k_list
    
# this solution is O(nlogn) because I used sorting
# you can get O(k log n) by using a heap!

# O(n) solution is found by using bucket sort! (technically O(2n) since you go through list and have to do an additional n operations through total list)

# second solution using bucket sort:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary for the count of each integer
        # create a list with n+1 indexes all with an empty array
        # iterate through the counter dictionary and enter the integer into the index
        # of the list that corresponds with its occurence count
        # iterate backwards from the end of the list and create the k list

        counter = {}
        # bucket_sort = [[]] * (len(nums) + 1)
        # NOTE: THIS IS A COMMON BUG! ALL OF THESE INDEXES ARE THE SAME INSTANCE
        # that's why I used the code below instead:
        bucket_sort = [[] for i in range(len(nums) + 1)]
        k_list = []

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        for key, value in counter.items():
            bucket_sort[value].append(key)

        for i in range(len(bucket_sort) -1, -1, -1):    #NOTE: -1 in second spot is to make sure it goes to 0, and -1 in third spot is increment
            while bucket_sort[i] and len(k_list) < k:
                k_list.append(bucket_sort[i].pop())
            if len(k_list) == k:
                break

        return k_list
    
# neetcode solution O(n):
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# heap solution: time complexity = O(k log n), space complexity = O(k + n)

# import heapq

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency = dict()
        
#         for num in nums:
#             value = frequency.get(num)
#             if value is None:
#                 value = 0      
#             frequency[num] = value + 1
            
#         kFrequent = heapq.nlargest(k, frequency.items(), key=lambda x:x[1])
#         elements = [num for num, freq in kFrequent]
        
#         return elements
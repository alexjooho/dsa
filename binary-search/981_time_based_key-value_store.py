class TimeMap:
    # hashmap with a key, and a list of values
    # each value in the list will be a pair (tuple) of the value and its time
    # NOTE: this is a good example of needing to read the fine print!
        # all timestamps of set are STRICTLY INCREASING, which means they will always be sorted!
    # instead of searching through entire list each time, we can do a binary search of the times
    # to find the max valid time

    # time complexity of set is O(1), time complexity of get is O(log n) since we're doing binary search

    # if middle value is <= timestamp, then update result and set left pointer to middle + 1
        # result will always get updated because every valid time will be the closest to timestamp
        # that we have seen so far in this binary search
    # else, set right pointer to middle - 1

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        # append to the list for the given key
        # tuple with (value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        # default result

        l, r = 0, len(self.hashmap[key]) - 1
        # REMEMBER TO DO LEN - 1!

        while l <= r:
            # edge case of empty list won't enter this while loop since r will start at - 1
            middle = (l + r) // 2
            value, time = self.hashmap[key][middle]
            if time == timestamp:
                return value
            elif time < timestamp:
                res = value
                l = middle + 1
            else:
                r = middle - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# neetcode solution:
# basically same solution but he just doesn't use defaultdict
# he checks if the key exists first, and if not, then creates a key value pair with an empty list
# he also doesn't cut the while loop short by checking if the time actually equals the timestamp

class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            # have to set an empty list if the key doesn't already exist
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        # uses get operation to return a list if the key doesn't already exist
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

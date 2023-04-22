class Node:
    def __init__(self, key, val):
        # initiate the node with its key, val, prev, and next
        # we need the key because we need to know the key to pop it from the cache!!!
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # to make the get and put methods run in O(1) time complexity,
    # we need to keep track of which key was used least recently
    # and we need to be able to update any key that is called to be the most recently used key

    # in order to do this, we need to use a double-edged linked list where
    # every node points to the NEXT and PREVIOUS nodes
    # we also need dummy nodes for the beginning and end of the linked list

    # using a hashmap:
    # for every key, we will set the value to the node it represents
    # if a key is replaced, remove that node from linked list and update the key's value with a new node
    # if a key is added and capacity is exceeded, then we remove the first node from our linked list

    # NOTE: deque uses a double linked list under the hood but it does not work efficiently since
    # removing a specific node using remove() takes O(n) time for a deque
    
    # NOTE: BE VERY METICULOUS ABOUT THE NEXT AND PREVIOUS FOR EACH NODE! Don't forget anything!

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        # these are the dummy nodes for head and tail
        # left = LRU, right = most recent
        self.left.next, self.right.prev = self.right, self.left
        # since we don't have any nodes at the start, the value after left dummy is the right dummy
        # and the value before the right dummy is the left dummy

    def remove(self, node):
        # helper function for removing node from linked list
        # remember to update both the next of prev and the prev of next!
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # helper function for inserting node to end of linked list (most recent)
        # have to update next for the previous last node
        # have to update prev and next for the inserted node
        # have to update prev for the right dummy node
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # if it exists, we have to update it to be the most recently used cache
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
            # remember that the value in the hashmap is actually the node, so we have to do .val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if the key already exists, remove it before inserting it
            node = self.cache[key]
            self.remove(node)

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # if the capacity is exceeded, then remove LRU
            # get the LRU by using the left dummy's next node
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
            # remember to remove it from both the linked list and the cache!

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# neetcode solution:
# same exact thing basically

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

class TrieNode:

    def __init__(self):
        self.children = {}
        # using hash map so its easy to search for the next letter in O(1) time
        # each new TrieNode starts off with no children
        # the value of each TrieNode isn't in the TrieNode itself, it's found in the previous node as a child
        self.end = False
        # using a boolean that we can change to true if this letter is also the end of a word
        # that was inserted
        # this is easier/smarter than putting a specific thing to look for in self.children to indicate ending of a word

class Trie:

    def __init__(self):
        self.root = TrieNode()
        # this is the base/root node that has no value but has all the children (up to 26 letters)

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.end
        # this will check if the final letter is the end of a word, which is the word we are searching for

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
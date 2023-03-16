class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str, cur = None) -> bool:
        cur = self.root if cur is None else cur
        # can't do cur = self.root as parameter of function since methods are created when class is created
        # don't have access to class properties until the function is called

        # if there is a '.', have to continue loop through every single child to check if the word exists
        # do this by recursively calling the function and inputting a current node
        for i in range(len(word)):
            if word[i] == '.':
                # if i == len(word) - 1:
                #     for node in cur.children.values():
                #         if node.end == True:
                #             return True
                #     return False
                # NOTE: Don't even need any of this logic, since if we find a '.', we check every char to see if it works
                for node in cur.children.values():
                    if self.search(word[i+1:], node):
                        return True
                return False
                # have to include this false in case a correct word is not found
            else:
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            
        return cur.end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# neetcode solution:
# my solution changed parameter of search function to include cur
# his solution simply makes another function that can be called recursively (but has same logic)

def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end

        return dfs(0, self.root)
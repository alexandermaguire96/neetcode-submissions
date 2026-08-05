#create TrieNode class in order to be able to move the root later
class TrieNode:
    def __init__(self):

        self.children = defaultdict(TrieNode)
        self.end = False

class PrefixTree:

    def __init__(self):

        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.end = True
        return


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.children:
                current = current.children[c]
            elif c not in current.children:
                return False
        if current.end:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            elif c not in current.children:
                return False
        return True
        
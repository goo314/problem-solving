class Trie:

    def __init__(self):
        self.val = None
        self.child = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        prev = self

        for c in word:
            if prev.child[ord(c)-ord('a')]:
                prev = prev.child[ord(c)-ord('a')]
                continue
            cur = Trie()
            cur.val = c
            prev.child[ord(c)-ord('a')] = cur
            prev = cur
        prev.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if not cur.child[ord(c)-ord('a')]:
                return False
            cur = cur.child[ord(c)-ord('a')]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if not cur.child[ord(c)-ord('a')]:
                return False
            cur = cur.child[ord(c)-ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

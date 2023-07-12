class TrieNode:
    def __int__(self):
        self.child=[None for i in range(26)]
        self.end=False
class Trie:
    def __int__(self):
        self.root=self.getNode()
    def getNode(self):
        return TrieNode()
    def char_index(self,ch):
        return int(ord(ch)-ord('a'))
    def insert(self,w):
        p=self.root
        length=len(w)
        for i in range(length):
            ind= self.char_index(w[i])
            if not p.child[ind]:
                p.child[ind]=self.getNode()
            p=p.child[ind]
        p.end=True

    def search(self, key):
        p = self.root
        length = len(key)
        for level in range(length):
            index = self.char_index(key[level])
            if not p.child[index]:
                return False
            p = p.child[index]

        return p.end
    def delete(self,key):
        p=self.root
        length=len(key)
        for i in range(length):
            index=self.char_index(key[i])
            if not p.child[index]:
                return
            p=p.child[index]
        p.end=False



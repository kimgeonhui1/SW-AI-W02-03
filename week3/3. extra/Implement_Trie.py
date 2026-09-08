class Trie(object):

    def __init__(self):
        self.tree = []

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.tree.append(word)
        print(self.tree)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for x in self.tree:
            if word == x:
                return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        for x in self.tree:
            if x[:len(prefix)] == prefix:
                return True    
        return False
        


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   
print(trie.search("app"))     
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
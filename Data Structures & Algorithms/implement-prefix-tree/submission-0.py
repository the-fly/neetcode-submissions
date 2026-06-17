class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnded = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            node.children[word[i]] = node.children.get(word[i], TrieNode())
            node = node.children[word[i]]
            # print(1, word[i])
        node.wordEnded = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if not word[i] in node.children:
                return False
            node = node.children[word[i]]
            # print(2, word[i])
        return node.wordEnded
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if not prefix[i] in node.children:
                return False
            node = node.children[prefix[i]]
        return True

        
        
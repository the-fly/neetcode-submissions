class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnded = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            node.children[word[i]] = node.children.get(word[i], TrieNode())
            node = node.children[word[i]]
        node.wordEnded = True

    def search(self, word: str) -> bool:
        node = self.root

        return self._search(word, node)
                

    def _search(self, word:str, node: Optional(TrieNode)) -> bool:
        # print(len(word), word, node.wordEnded)
        if not node:
            return False
        if len(word) == 0:
            return node.wordEnded
        
        
        if word[0] == '.':
            for child in node.children:
                if self._search(word[1:], node.children[child]):
                    return True
            return False

        if word[0] in node.children:
            return self._search(word[1:], node.children[word[0]])
        return False

# https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/1401287550

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.flag_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.flag_word = True

    def search(self, word: str) -> bool:
        return self.searchNode(word, 0, self.root)
    
    def searchNode(self, word, i, node):
        if i == len(word):
            return node.flag_word
        
        char = word[i]
        
        if char == ".":
            for child in node.nodes.values():
                if self.searchNode(word, i + 1, child):
                    return True
            return False

        else:
            if char not in node.nodes:
                return False
            return self.searchNode(word, i + 1, node.nodes[char])
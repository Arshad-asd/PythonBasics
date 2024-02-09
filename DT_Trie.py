class TrieNode:
    def __init__(self):
        self.childern = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.childern:
                node.childern[char] = TrieNode()
            node = node.childern[char] 
        node.end_of_word = True
    def display(self):
        word = []
        def dfs(node,prefix):
            if node.end_of_word:
                word.append(prefix)
            for char in node.childern:
                dfs(node.childern[char],prefix+char)
        dfs(self.root,'')
        print(word)
    def prefix_related(self,prefix):
        word = []
        node = self.root
        for char in prefix:
            if char not in node.childern:
                return None
            node = node.childern[char]
        def dfs(node,current_prefix):
            if node.end_of_word:
                word.append(current_prefix)
            for char,child in node.childern.items():
                dfs(child,current_prefix+char)
        dfs(node,prefix)
        print(word)

trie = Trie()
trie.insert('app')
trie.insert('apps')
trie.insert('apple')
trie.insert('banana')
trie.display()
trie.prefix_related('b')

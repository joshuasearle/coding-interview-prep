class TrieNode(object):
    def __init__(self):
        self.end_of_word = False
        self.children = [None for _ in range(26)]
    
    @staticmethod
    def char_to_index(char):
        return ord(char) - ord('a')
    
    @staticmethod
    def index_to_char(index):
        return chr(index - ord('a'))
    
    def __setitem__(self, char, node):
        self.children[TrieNode.char_to_index(char)] = node
    
    def __getitem__(self, char):
        return self.children[TrieNode.char_to_index(char)]

    def __contains__(self, char):
        return self[char] is not None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = TrieNode()
            current = current[char]
        current.end_of_word = True
    
    def __contains__(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return current.end_of_word

words = ['hello', 'world', 'bye', 'lsdjf', 'lsjdflksj', 'byebye', 'hi', 'no', 'noway']

t = Trie()
for word in words:
    t.add_word(word)

print('hello' in t)
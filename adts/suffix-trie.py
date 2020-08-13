from trie import Trie

class SuffixTrie(object):
    def __init__(self, word):
        self.trie = Trie()
        word_list = list(word)
        for _ in range(len(word_list)):
            self.trie.add_word(''.join(word_list))
            word_list.pop(0)
        self.trie.add_word('')
        

    def __contains__(self, word):
        return word in self.trie

t = SuffixTrie('hello')
print(t.trie.root.end_of_word)
print('ello' in t)
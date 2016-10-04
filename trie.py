class Trie(object):
    def __init__(self, char, word):
        self.char = char
        self.sons = []
        self.word = word
    def add(self, string):
        self.word += 1
        father = self
        for char in string:
            for son in father.sons:
                if son.char == char:
                    son.word += 1
                    father = son
                    break
            else:
                son = Trie(char, 1)
                father.sons.append(son)
                father = son
        return
    def find(self, string):
        father = self
        for char in string:
            for son in father.sons:
                if son.char == char:
                    father = son
                    break
            else:
                return 0
        return father.word

# create a new Trie
t = Trie('', 0)
# add some words to Trie
t.add('fee')
t.add('fi')
t.add('fo')
t.add('fum')
# search for prefixes in our Trie
print(t.find('f'))

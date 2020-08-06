class Node:
    def __init__(self):
        self.count = 0
        self.prefix = 0
        self.next = None

class TrieTree:
    def __init__(self):
        self.root = Node()
        self.root.next = [Node() for _ in range(26)]

    def insert(self, s: str):
        temp = self.root.next
        for i in range(len(s)):
            temp[ord(s[i])-97].prefix += 1
            if i == len(s)-1:
                temp[ord(s[i]) - 97].count += 1
            else:
                if temp[ord(s[i])-97].next is None:
                    temp[ord(s[i]) - 97].next = [Node() for _ in range(26)]
                temp = temp[ord(s[i]) - 97].next

    def search(self, s: str):
        temp = self.root.next
        for i in range(len(s)):
            if i == len(s)-1:
                return temp[ord(s[i])-97].count
            if temp[ord(s[i])-97].prefix == 0:
                return 0
            temp = temp[ord(s[i])-97].next

s = TrieTree()
s.insert('asdalksjd')
s.insert('zxciouqwe')
s.insert('zxcqwe')
s.insert('zxc')
s.insert('qwe')
s.insert('zxc')
print(s.search('z'))
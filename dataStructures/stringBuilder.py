class StringBuilder():
    def __init__(self) -> None:
        self.strs = []

    def add(self, val):
        self.strs.append(val)

    def toString(self):
        return "".join(self.strs)


s = StringBuilder()
s.add('This')
s.add('is')
s.add('a')
s.add('new')
s.add('string builder')
print(s.toString())

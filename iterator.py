class my_enumerate:
    def __init__(self, some_iter):
        self.some_iter = iter(some_iter)
        self.count = -1
    def __iter__(self):
        return self
    def next(self):
        val = self.some_iter.next()
        self.count += 1
        return self.count, val
    
for n, val in my_enumerate(['a', 'b', 'c']):
    print(n, val)
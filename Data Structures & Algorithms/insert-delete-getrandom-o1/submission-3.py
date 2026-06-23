class RandomizedSet:

    def __init__(self):
        self.l = []
        self.n = 0
        self.m = {}

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        else:
            if len(self.l) <= self.n:
                self.l.append(val)
            else:
                self.l[self.n] = val

            self.m[val] = self.n
            self.n += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        else:
            idx = self.m[val]
            del self.m[val]
            last_elem = self.l[self.n-1]
            self.l[idx] = last_elem
            self.m[last_elem] = idx
            self.n -= 1
            return True

    def getRandom(self) -> int:
        n = random.randint(0, self.n-1)
        print(self.m)
        return self.l[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
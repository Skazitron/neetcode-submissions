class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.m: return False
        self.arr.append(val)
        self.m[val] = len(self.arr) - 1
        

    def remove(self, val: int) -> bool:
        if val not in self.m: return False
        # we need to swap the values in the array
        # we also need to update the idx of the former end value in the map
        # with the idx of the value to be removed
        rem_idx = self.m[val]
        last_val = self.arr[-1]
        self.m[last_val] = rem_idx
        del self.m[val]
        self.arr[-1], self.arr[rem_idx] = self.arr[rem_idx], self.arr[-1]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.arr) - 1)
        return self.arr[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
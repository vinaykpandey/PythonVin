class HashTale:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash%100

    def get(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def add(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

    def delete(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

t = HashTale()
t.add("name", "vinay")
# print(t.get("name"))
t["age"] = 34
print(t["name"])
print(t["age"])



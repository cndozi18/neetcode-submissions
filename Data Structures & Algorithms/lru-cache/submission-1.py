class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] =val
            print(f"get {key} : {self.cache[key]}")
            return val
        else:
            print(f"{key} not in cache")
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return
        if len(self.cache) >= self.capacity:
            for k, v in self.cache.items():
                print(f"{k} is the LRU value")
                del self.cache[k]
                break
        print(f"put {key} : {value} into cache")
        self.cache[key] = value

class Hashmap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX  # MAX is the size of array. So we want indices from 0 to 9 that's why we did sum%10

    def add(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

    def get_data(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def delete(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

hash_map = Hashmap()
hash_map.add('march 6', 200)
hash_map.add('march 5', 300)
hash_map.add('march 13', 400)
hash_map.add('march 12', 400)
hash_map.add('feb 11', 400)
hash_map.add('march 17', 999)
hash_map.add('jan 12', 400)
hash_map.add('april 13', 400)
hash_map.delete('april 13')
print(hash_map.get_data('april 13'))

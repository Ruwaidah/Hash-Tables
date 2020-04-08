# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            # find storage with no data
            while pair is not None:
                # replace the value if key already exist
                if pair.key == key:
                    pair.value = value
                    return
                elif pair.next:
                    # check next node
                    pair = pair.next
                else:
                    pair.next = LinkedPair(key, value)
                    return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None and self.storage[index].key == key:
            self.storage[index] = None
        else:
            print("Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.

        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        if pair is None:
            return None
        else:
            while pair is not None:
                if pair.key == key:
                    return pair.value
                elif pair.next:
                    pair = pair.next
                else:
                    return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.

        '''

        # Doubles capacity
        self.capacity *= 2
        # make a new storage with Doubles capacity
        new_storage = [None] * self.capacity
        # set old storage  before increasing it
        old_storage = self.storage
        self.storage = new_storage
        for node in old_storage:
            if node:
                self.insert(node.key, node.value)
                pair = node
                while pair.next:
                    pair = pair.next
                    self.insert(pair.key, pair.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")
    print("ht", ht.storage)
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # print("")

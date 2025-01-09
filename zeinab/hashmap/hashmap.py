class HashMap:
    def __init__(self, size=10):
        # Initialize the hash map with a fixed size
        self.size = size
        self.map = [None] * self.size

    def _hash(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def add(self, key, value):
        """Add a key-value pair to the hash map."""
        key_hash = self._hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.map[key_hash].append(key_value)

    def get(self, key):
        """Retrieve a value by its key."""
        key_hash = self._hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """Remove a key-value pair from the hash map."""
        key_hash = self._hash(key)
        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if pair[0] == key:
                    self.map[key_hash].pop(i)
                    if not self.map[key_hash]:  # Remove empty bucket
                        self.map[key_hash] = None
                    return
        print("Key not found")

    def keys(self):
        """Return a list of all keys in the hash map."""
        keys = []
        for bucket in self.map:
            if bucket is not None:
                for pair in bucket:
                    keys.append(pair[0])
        return keys

    def values(self):
        """Return a list of all values in the hash map."""
        values = []
        for bucket in self.map:
            if bucket is not None:
                for pair in bucket:
                    values.append(pair[1])
        return values

    def __str__(self):
        """Return a string representation of the hash map."""
        result = ""
        for i, bucket in enumerate(self.map):
            if bucket is not None:
                result += f"Bucket {i}: {bucket}\n"
        return result or "HashMap is empty"

# Test cases for the HashMap class
if __name__ == "__main__":
    # Create a hash map instance
    hash_map = HashMap(size=5)

    # Test adding key-value pairs
    hash_map.add("name", "Alice")
    hash_map.add("age", 30)
    hash_map.add("city", "Tehran")
    hash_map.add("job", "Engineer")

    print("After adding elements:")
    print(hash_map)

    # Test retrieving values
    assert hash_map.get("name") == "Alice", "Test case failed for get(name)"
    assert hash_map.get("age") == 30, "Test case failed for get(age)"
    assert hash_map.get("city") == "Tehran", "Test case failed for get(city)"

    # Test updating a value
    hash_map.add("age", 31)
    assert hash_map.get("age") == 31, "Test case failed for updating age"

    # Test deleting a key
    hash_map.delete("city")
    assert hash_map.get("city") is None, "Test case failed for delete(city)"

    print("After deleting 'city':")
    print(hash_map)

    # Test keys and values retrieval
    assert set(hash_map.keys()) == {"name", "age", "job"}, "Test case failed for keys()"
    assert set(hash_map.values()) == {"Alice", 31, "Engineer"}, "Test case failed for values()"

    print("All test cases passed!")

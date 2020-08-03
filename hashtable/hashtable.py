class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.load = 0


    # MONDAY
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    # MONDAY
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity


    # MONDAY
    def fnv1_64(self, string, seed=0):
        """
        Returns: The FNV-1, 64-bit hash of a given string. 
        """
        #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in string:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    # MONDAY
    def fnv1a_64(self, string, seed=0):
        """
        Returns: The FNV-1a (alternate) hash of a given string
        """
        #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in string:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash


    # MONDAY
    def djb2(self, key):
        """
        Returns: The DJB2 hash, 32-bit hash of a given string.
        """
        # Your code here
        return self.capacity


    # MONDAY
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # Alternate between which of the following (2) you'd like to use:
        return self.fnv1_64(key) % self.capacity
        #return self.djb2(key) % self.capacity


    # MONDAY
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Hash the key
        hashed_index = self.hash_index(key)

        # If hashed key doesn't already exist in data...
        if self.data[hashed_index] == None:
            # then make a new HashTableEntry and add it to the index of the hashed key.
            self.data[hashed_index] = HashTableEntry(key, value)
            # For keeping track of how many elements are indexed in this hash table:
            self.load += 1
        else:
            node = self.data[hashed_index]
            if node.key == key:
                node.value = value
            else:
                while node.next != None and node.key != key:
                    node = node.next
                node.next = HashTableEntry(key, value)
                self.load += 1
        
        #if self.get_load_factor() > 0.7:
        #    self.resize(2*self.capacity)
        

    # MONDAY
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Hash the key
        hashed_index = self.hash_index(key)

        # If hashed key doesn't exist in data...
        if self.data[hashed_index] == None: 
            print("ERROR: Key not found in list.")

        elif self.data[hashed_index].key == key:
            self.data[hashed_index] = None
            # For keeping track of how many elements are indexed in this hash table:
            self.load -= 1

        elif (self.data[hashed_index].key != key) and (self.data[hashed_index].next != None):
            prev = self.data[hashed_index]
            curr = self.data[hashed_index].next
            while curr.key != key and curr.next != None:
                prev, curr = curr, curr.next
            if curr.key == key:
                prev.next = curr.next
                # For keeping track of how many elements are indexed in this hash table:
                self.load -= 1

    # MONDAY
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # Hash the key
        hashed_index = self.hash_index(key)

        # Fetch the data
        data = self.data[hashed_index]

        # If None, return None...
        if data == None:
            return data
        
        while data.key != key and data.next != None:
            data = data.next
        if data.key == key:
            return data.value 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

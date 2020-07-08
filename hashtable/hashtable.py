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
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if(self.storage[index] == None):
            self.storage[index] = HashTableEntry(key, value)
            self.size +=1
        else:
            #check if it exists already
            curr = self.storage[index]
            while curr.next != None and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            #it doesn't exist already, so add it to the head of the list
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.storage[index]
                self.storage[index] = new_entry
                self.size +=1
        



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        
        if self.storage[index].key == key:
            #if it was only one in the list
            if self.storage[index].next == None:
                #list should now be empty
                self.storage[index] = None
                self.size -=1
            #it is not the only one in the list
            else:
                new_head = self.storage[index].next
                self.storage[index].next = None
                self.storage[index] = new_head
                self.size -=1
        #node was not first in the list or is none
        else:
            if self.storage[index] == None:
                return None
            else:
                curr = self.storage[index]
                prev = None
                #search until at end or have found key
                while curr.next is not None and curr.key != key:
                    prev = curr
                    curr = curr.next
                #found the key
                if curr.key == key:
                    prev.next = curr.next
                    self.size -=1
                    return curr.value
                #didn't find the key
                else:
                    return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        #if its the head
        if self.storage[index] is not None and self.storage[index].key == key:
            return self.storage[index].value
        elif self.storage[index] is None:
            return None
        else:
            curr = self.storage[index]
            while curr.next != None and curr.key != key:
                curr = self.storage[index].next
            if curr == None:
                return None
            else:
                return curr.value


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

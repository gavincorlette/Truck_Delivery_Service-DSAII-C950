
# Code is from WGU Webinar 1 - Let's Go Hashing

# HashTable class
class HashTable:
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity = 40):
        # Initialize the hash table with empty bucket list entries
        self.array = []
        for i in range(initial_capacity):
            self.array.append([])

    def search_for(self, key):
        # Get the bucket list where the key would be
        bucket = hash(key) % len(self.array)
        bucket_list = self.array[bucket]

        # Search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    def insert_into(self, key, item):
        # Get the bucket list where this item will go
        bucket = hash(key) % len(self.array)
        bucket_list = self.array[bucket]

        # Update key if it is already in the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # Else, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def remove_from(self, key):
        # Get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.array)
        bucket_list = self.array[bucket]

        # Remove the item from the bucket list if it is present
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max = limit
        self.size = 0
        self.storage = {}
        self.list = DoublyLinkedList()
    
    # Solution from Wednesday Lecture
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList
        self.storage = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Check for elements, if nothing exists, return None
        if not self.list.head and not self.list.tail:
            return None
        key_value = self.get_node(key)
        if key_value:
            self.list.move_to_front(key_value)
            for value in self.storage:
                if value == key:
                    return self.storage[value]
        else:
            return None


    # def get(self, key):
    #     if key in self.storage:
    #         valid_key = self.storage[key]
    #         self.list.delete(valid_key)
    #         self.list.add_to_head(valid_key)
    #         return valid_key.value
    #     else:
    #         return None

    # Solution from Wednesday's lecture
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        key_value = self.get_node(key)
        if key_value:
            for x in self.storage:
                if x == key:
                    self.storage[x] = value
            self.list.move_to_front(key_value)
        else:
            if self.size >= self.max:
                current_tail = self.list.remove_from_tail()
                self.storage.pop(current_tail)
            new_list = self.list.add_to_head(key)
            self.storage.update({key: value})
            self.size = self.list.length
            return new_list

    # def set(self, key, value):
    #     if key in self.storage:
    #         valid_key = self.storage[key]
    #         valid_key.value = value

    #         if self.list.head is not valid_key:
    #             self.list.delete(valid_key)
    #             self.list.add_to_head(valid_key)
    #     else:
    #         new_list_node = DoublyLinkedList(value)
    #         if self.list.get_max() == self.limit:
    #             self.storage.pop(key)
    #         self.list.add_to_head(new_list_node)
    #         self.storage[key] = new_list_node

    # Helper Function to find the node
    def get_node(self, key):
        current_head = self.list.head
        found_node = False
        
        while current_head and found_node == False:
            if current_head.value == key:
                found_node = True
            else:
                current_head = current_head.next
        if not found_node:
            current_head = None
        return current_head

    # Solution from Wednesday's lecture
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
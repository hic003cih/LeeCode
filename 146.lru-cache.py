#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict
class LRUCache:
    #Least Recently Used,LRU
    # #1. Use OrderedDict(Pythonic)
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.cache = OrderedDict()

    # def get(self, key: int) -> int:
    #     #Check if the key exists in the cache
    #     if key not in self.cache:
    #         return -1
    #     #Mark as recently used by moving it to the end.
    #     self.cache.move_to_end(key)
    #     return self.cache[key]
        

    # def put(self, key: int, value: int) -> None:
    #     # If key already exists, update the value and mark as recently used.
    #     if key in self.cache:
    #         self.cache[key] = value
    #         self.cache.move_to_end(key)
    #     else:
    #         # If the cache is full, evict the least recently used item.
    #         # In the an OrderedDict, the item inserted first is at the front.
    #         if len(self.cache) >= self.capacity:
    #             self.cache.popitem(last=False)
            
    #         #Insert the new item.
    #         self.cache[key] = value
	
    # 2. Hash Map / Dictionary + linked List

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> node
        # Use dummy head and tail for easier node removal/addition
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        # Helper to remove a node from the list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node):
        # Helper to add a node to the front of the list
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # If key exists, move it to head (most recently used) and return its value
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_head(node)
            return node.value
        return -1
    def put(self, key: int, value: int) -> None:
        # If key already exists, update its value and move it to head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # If cache is full, remove the least recently used item (the tail)
            if len(self.cache) >= self.capacity:
                tail_node = self.tail.prev
                self._remove_node(tail_node)
                del self.cache[tail_node.key]
            
            # Create a new node and add it to the head of the list and to the cache
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

# Node for the Doubly Linked List
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
	
	
	

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


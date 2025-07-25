#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from typing import Dict
import collections
class LFUCache:
    # LFU Least Frequently Used
    # # 1. Brute-force
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     # Dictionary to store key -> value
    #     self.vals: Dict[int, int] = {}
    #     # Dictionary to store key -> frequency
    #     self.freqs: Dict[int, int] = {}
    #     # Dictionary to store key -> last access time
    #     self.recency: Dict[int, int] = {}
    #     # A global timer to track recency
    #     self.timer = 0
    
    # def _update_recency(self, key:int):
    #     """ Helper function to update the timestamp for a key."""
    #     self.timer +=1
    #     self.recency[key] = self.timer

    # def get(self, key: int) -> int:
    #     if key not in self.vals:
    #         return -1
    #     # Increment frequency
    #     self.freqs[key] +=1
    #     # Update recency
    #     self._update_recency(key)
    #     return self.vals[key]

    # def put(self, key: int, value: int) -> None:
    #     if self.capacity ==0:
    #         return
    #     # If key already exists
    #     if key in self.vals:
    #         self.vals[key] = value
    #         self.freqs[key] +=1
    #         self._update_recency(key)
    #         return
    #     # If cache is full, we must evict a key
    #     if len(self.vals) >= self.capacity:
    #         # 1. Find the minimum frequency
    #         min_freq = min(self.freqs.values())

    #         # 2. Find all keys with that minimum frequency
    #         lfu_keys = [k for k,v in self.freqs.items() if v == min_freq]

    #         # 3. Among them, find the one with the smallest timestamp (Least Recently Used)
    #         key_to_evict = min(lfu_keys,key=lambda k:self.recency[k])

    #          # 4. Evict the key from all dictionaries
    #         del self.vals[key_to_evict]
    #         del self.freqs[key_to_evict]
    #         del self.recency[key_to_evict]
        
    #     # Add the new key-value pair
    #     self.vals[key] = value
    #     self.freqs[key] = 1
    #     self._update_recency(key)

    # Hash Map + Double linked List Node
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_node = {}  # key -> DLinkedNode
        self.freq_to_dll = collections.defaultdict(DLinkedList)
        self.min_freq = 0
    
    def _update_node_freq(self, node):
        #1. Remove node from its old frequency list
        old_freq = node.freq
        self.freq_to_dll[old_freq].remove_node(node)

        # 2. If the old frequency list is now empty and it was the minimum, update min_freq
        if self.min_freq == old_freq and self.freq_to_dll[old_freq].size ==0:
            self.min_freq +=1
        
        # 3. Increase node's frequency and add it to the new frequency list.
        node.freq +=1
        new_freq = node.freq
        self.freq_to_dll[new_freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_node_freq(node)
        return node.val
    

    def put(self, key: int, value: int) -> None:
        if self.capacity ==0:
            return
        if key in self.key_to_node:
            # Key exists, update value and frequency
            node = self.key_to_node[key]
            node.val = value
            self._update_node_freq(node)
        else:
            # Key is new
            #Check if cache is full
            if self.size >= self.capacity:
                lfu_list = self.freq_to_dll[self.min_freq]
                node_to_evict = lfu_list.remove_tail()
                if node_to_evict:
                    del self.key_to_node[node_to_evict.key]
                    self.size -=1
            # Add the new node
            new_node = DLinkedNode(key,value)
            self.key_to_node[key] = new_node
            self.freq_to_dll[1].add_to_head(new_node)
            self.min_freq = 1
            self.size +=1

            
    
# Doubly Linked List Node
class DLinkedNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

# Doubly Linked List for each frequency group
class DLinkedList:
    def __init__(self):
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    def remove_tail(self):
        if self.size > 0:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node
        return None
    

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


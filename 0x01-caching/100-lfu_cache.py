#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache is a caching system that inherits from BaseCaching.

    This class implements an LFU caching system where the least frequently
    used item is removed when the cache exceeds the defined MAX_ITEMS limit.
    If there is a tie, the least recently used item among the tied items is discarded.
    """

    def __init__(self):
        """
        Initialize the LFU cache.
        """
        super().__init__()
        self.usage_count = {}  # To keep track of how often each key is used
        self.keys_order = []   # To keep track of the order of keys for LRU

    def put(self, key, item):
        """
        Add an item in the cache using LFU algorithm.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to be stored in the cache.

        If key or item is None, this method does nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, the least
        frequently used item is discarded. If there's a tie, the least
        recently used item among them is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and usage count
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.keys_order.remove(key)  # Remove to update order later
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_usage = min(self.usage_count.values())
                lfu_keys = [k for k, v in self.usage_count.items() if v == min_usage]

                # If there's a tie, use LRU by checking keys_order
                if len(lfu_keys) > 1:
                    # The first LFU key in the keys_order list is the LRU among LFUs
                    lfu_key = next(k for k in self.keys_order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                # Discard the LFU (or LRU among LFU) key
                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                self.keys_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item and initialize its usage count
            self.cache_data[key] = item
            self.usage_count[key] = 1

        # Update the order of keys to mark the current key as most recently used
        self.keys_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if the key is not
                 found or if key is None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the usage count and the order to mark the key as recently used
        self.usage_count[key] += 1
        self.keys_order.remove(key)
        self.keys_order.append(key)
        return self.cache_data[key]

#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache is a caching system that inherits from BaseCaching.

    This class implements an LRU caching system where the least recently
    used item is removed when the cache exceeds the defined MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the LRU cache.
        """
        super().__init__()
        self.keys_order = []  # To keep track of the order of keys for LRU

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to be stored in the cache.

        If key or item is None, this method does nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, the least
        recently used item is discarded.
        """
        if key is None or item is None:
            return

        # If key already exists, remove it first to update its order later
        if key in self.cache_data:
            self.keys_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LRU: Remove the least recently used item
            least_recently_used_key = self.keys_order.pop(0)
            del self.cache_data[least_recently_used_key]
            print(f"DISCARD: {least_recently_used_key}")

        # Add the new item
        self.cache_data[key] = item
        self.keys_order.append(key)  # Mark this key as most recently used

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

        # Update the order to mark the key as recently used
        self.keys_order.remove(key)
        self.keys_order.append(key)
        return self.cache_data[key]


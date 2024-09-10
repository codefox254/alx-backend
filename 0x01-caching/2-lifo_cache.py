#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.

    This class implements a LIFO caching system where the last added item is
    removed when the cache exceeds the defined MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        """
        super().__init__()
        self.keys_order = []  # To keep track of the order of keys for LIFO

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to be stored in the cache.

        If key or item is None, this method does nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, the last item
        added is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item, no change in order
            self.cache_data[key] = item
        else:
            # Add new item
            self.cache_data[key] = item
            self.keys_order.append(key)

            # Check if we need to discard the last added item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # LIFO: Remove the last key in the order list
                last_key = self.keys_order.pop(-2)  # Remove the second-last (previous) item
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if the key is not found or if key is None.
        """
        return self.cache_data.get(key)

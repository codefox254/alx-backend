#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching.

    This class implements a FIFO caching system where items are added in the
    order they are received, and the oldest item is removed when the cache
    exceeds the defined MAX_ITEMS limit.
    """

    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()
        self.keys_order = []  # To keep track of the order of keys for FIFO

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to be stored in the cache.
        
        If key or item is None, this method does nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, the oldest item
        (first added) is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and maintain the order
            self.cache_data[key] = item
        else:
            # Add new item
            self.cache_data[key] = item
            self.keys_order.append(key)

            # Check if we need to discard the oldest item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO: Remove the first key in the order list
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if the key is not found or if key is None.
        """
        return self.cache_data.get(key)

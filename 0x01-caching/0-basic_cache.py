#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.

    This class implements a basic cache with no limit on the number of items
    it can store. Items are stored in the cache_data dictionary inherited
    from BaseCaching.
    """

    
    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to be stored in the cache.
        
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    
    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if the key is not found or if key is None.
        """
        return self.cache_data.get(key)

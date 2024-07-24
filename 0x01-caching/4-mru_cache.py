#!/usr/bin/env python3
"""
Module for MRUCache that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements a caching system with MRU replacement policy.
    """

    def __init__(self):
        """
        Initialize the class instance and inherit from BaseCaching.
        """
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """
        Add or update the cache. If the cache exceeds the max limit,
        removes the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove key from current position-> it will be updated
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add/Update the key at the end of the order list
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Return the value linked to key in the cache_data. Move the key to
        the end of the order list to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end to mark it as most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)

#!/usr/bin/env python3
"""
Module for MRUCache that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements caching system with MRU replacement policy.
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
                self.cache_data[key] = item
                self.order.remove(key)
                self.order.append(key)
            else:
                self.cache_data[key] = item
                self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Return the value linked to key in the cache_data. Move the key to
        the end of the order list to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)

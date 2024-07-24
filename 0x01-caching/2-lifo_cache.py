#!/usr/bin/env python3
"""
Module for LIFOCache that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a caching system with LIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance and inherit from BaseCaching.
        """
        super().__init__()
        self.last_key = None  # To keep track of the last item added

    def put(self, key, item):
        """
        Add or update the cache. If the cache exceeds the max limit,
        removes the last item entered based on LIFO.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if self.last_key and len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.last_key
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.last_key = key

    def get(self, key):
        """
        Return the value linked to key in the cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

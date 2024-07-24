#!/usr/bin/env python3
"""
Module for FIFOCache that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a caching system with FIFO algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance and inherit from BaseCaching.
        """
        super().__init__()
        self.order = []  # To keep track of the order of items for FIFO

    def put(self, key, item):
        """
        Add or update the cache. If the cache exceeds the max limit,
        removes the first item entered.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.append(key)  # Update the order
                self.order.remove(key)  # Maintain the order
            else:
                self.cache_data[key] = item
                self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """
        Return the value linked to key in the cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

#!/usr/bin/env python3
"""
Module for BasicCache that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache implements a basic caching system.
    """

    def put(self, key, item):
        """
        Assign the item value for the key `key` in the cache_data dictionary.
        Does nothing if key or item is None.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to key in the cache_data dictionary.
        Returns None if key is None or key is not present in the cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

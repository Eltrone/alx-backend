#!/usr/bin/env python3
"""
Module for LFUCache that inherits from BaseCaching.
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache implements a caching system with LFU replacement policy.
    """

    def __init__(self):
        """
        Initialize the class instance and inherit from BaseCaching.
        """
        super().__init__()
        self.usage_counts = defaultdict(int)
        self.lfu = {}
        self.min_freq = 0

    def put(self, key, item):
        """
        Add or update the cache. If the cache exceeds the max limit,
        removes the least frequently used item. If there's a tie,
        the least recently used item of the least frequently used
        group is removed.,
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.get(key)  # Update frequency
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.lfu[self.min_freq]))
                del self.cache_data[oldest_key]
                del self.usage_counts[oldest_key]
                self.lfu[self.min_freq].pop(oldest_key)
                print(f"DISCARD: {oldest_key}")

            self.cache_data[key] = item
            self.usage_counts[key] = 1
            if 1 not in self.lfu:
                self.lfu[1] = OrderedDict()
            self.lfu[1][key] = True
            self.min_freq = 1

    def get(self, key):
        """
        Return the value linked to key in the cache_data.
        Updates the frequency of the key.
        """
        if key not in self.cache_data:
            return None
        freq = self.usage_counts[key]
        self.usage_counts[key] += 1
        self.lfu[freq].pop(key)
        if not self.lfu[freq]:
            del self.lfu[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        if freq + 1 not in self.lfu:
            self.lfu[freq + 1] = OrderedDict()
        self.lfu[freq + 1][key] = True
        return self.cache_data[key]

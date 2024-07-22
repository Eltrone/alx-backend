#!/usr/bin/env python3
"""
This module contains a Server class for paginating a database of popular
baby names with hypermedia support.
"""

import csv
import math
from typing import List, Dict

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for a page of items.
    :param page: Page number, 1-indexed
    :param page_size: Items per page
    :return: Tuple with start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names with hypermedia."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetch a page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index] if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Fetch a page and return hypermedia pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_entries = len(self.dataset())
        total_pages = math.ceil(total_entries / page_size)
        next_page = page + 1 if page * page_size < total_entries else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

if __name__ == "__main__":
    # Testing the Server's hypermedia pagination method
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))

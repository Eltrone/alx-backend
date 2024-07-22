#!/usr/bin/env python3
"""
This module contains a Server class for paginating a database of popular
baby names.
"""

import csv
from typing import List

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
    """Server class to paginate a database of popular baby names."""
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
        :param page: Page number, defaults to 1
        :param page_size: Items per page, defaults to 10
        :return: List of rows for specified page
        """
        assert isinstance(page, int) and page > 0, "page must be a positive int"
        assert isinstance(page_size, int) and page_size > 0,\
            "page_size must be a positive int"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index] if start_index < len(dataset) else []


if __name__ == "__main__":
    # Testing the Server's pagination method
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised with non-ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))

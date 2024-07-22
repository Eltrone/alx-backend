#!/usr/bin/env python3
"""
provides a function to calculate start and end indices for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a page of items.
    :param page: The page number, 1-indexed
    :param page_size: The number of items per page
    :return: A tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction
    index_range = __import__('0-simple_helper_function').index_range

    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)

#!/usr/bin/env python3
"""Task 2: Hypermedia pagination implementation.
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indices for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to handle pagination for a dataset of baby names.
    
    Attributes:
        DATA_FILE (str): Path to the CSV file containing the dataset.
        __dataset (List[List]): Internal storage for the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows representing the requested page of data.
        """
        assert type(page) == int and type(page_size) == int, "Page and page size must be integers."
        assert page > 0 and page_size > 0, "Page and page size must be greater than 0."
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve hypermedia pagination details for a specific page.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination details including current page, page size, data, next and previous page numbers, and total pages.
        """
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages
        }

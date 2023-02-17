#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems and Deep Learning in Python                                     #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /recsys/neighborhood/indices.py                                                     #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/recsys-deep-learning-udemy                         #
# ------------------------------------------------------------------------------------------------ #
# Created    : Friday February 17th 2023 05:36:07 am                                               #
# Modified   : Friday February 17th 2023 01:03:41 pm                                               #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
"Module for User, Item, Common Item, and Common User indices" ""
import sys
from recsys.neighborhood.base import Index


# ------------------------------------------------------------------------------------------------ #
class Cooccurrence(Index):
    """Class contains users and items that co-occur in the form of a rating.

    Args:
        index (dict): dictionary containing user-item or item-user co-occurrence
        user(bool): Indicates whether the mapping is from user to items. Default is True.
            If False, the co-occurrence is item_user.

    """

    def __init__(self, index: dict, user: bool = True) -> None:
        super().__init__()
        self._user = user
        self._index = index
        self._name = "user_item_cooccurrence_index" if user else "item_user_cooccurrence_index"

    def __len__(self) -> int:
        """Total number of items in the index"""
        return len(self._index)

    @property
    def size(self) -> int:
        """Total size of index in memory"""
        return sys.getsizeof(self._index)

    def search(self, key: int) -> list:
        """Returns the values associated with the key, i.e. items associated with an index or vice-versa

        Args:
            key (int): The useridx or itemidx value used as the key in the co-occurrence index.
        """
        return self._index[key]


# ------------------------------------------------------------------------------------------------ #
class Coreference(Index):
    """Class containing users or items that coreference the same item or user via a rating.

    Args:
        index (dict): The coreference dictionary
        user (bool): Whether the coreference is between users or items.
    """

    def __init__(self, index: dict, user: bool = True) -> None:
        super().__init__()
        self._user = user
        self._index = index
        self._name = "user_coreference_index" if user else "item_coreference_index"

    def __len__(self) -> int:
        """Total number of items in the index"""
        return len(self._index)

    @property
    def size(self) -> int:
        """Total size of index in memory"""
        return sys.getsizeof(self._index)

    def search(self, a: int, b: int) -> list:
        """Returns the value associated with the a_b tuple pair

        Args:
            a (int): Either a useridx or itemidx.
            b (int): Either a useridx or itemidx
        """
        key = (a, b) if a < b else (b, a)
        return self._index[key]

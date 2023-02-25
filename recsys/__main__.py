#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Recommender Systems and Deep Learning in Python                                     #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.6                                                                              #
# Filename   : /recsys/__main__.py                                                                 #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/recsys-deep-learning                               #
# ------------------------------------------------------------------------------------------------ #
# Created    : Sunday January 29th 2023 09:08:36 am                                                #
# Modified   : Friday February 24th 2023 09:30:12 pm                                               #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from recsys.container import Recsys


# ------------------------------------------------------------------------------------------------ #
def wireup():
    container = Recsys()

    container.init_resources()

    container.wire(
        modules=[__name__, "recsys.operator.base"],
    )


def main():
    wireup()


# ------------------------------------------------------------------------------------------------ #
if __name__ == "__main__":
    main()

#!/bin/python

import pytest
from baseball_id import lookup
import os


@pytest.fixture()
def lookup_obj():
    lk = lookup.Cache()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lk.set_source("{}/sample.master.csv".format(dir_path))
    yield lk

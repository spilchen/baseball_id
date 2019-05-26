#!/bin/python

import pytest
from baseball_id.factory import Factory


@pytest.fixture()
def lookup_obj():
    yield Factory.create_fake()

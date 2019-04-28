#!/bin/python

import pytest


def test_lookup_AaronHill(lookup_obj):
    s = lookup_obj.mlb_id(431094)
    assert(s.mlb_name == 'Aaron Hill')


def test_lookup_bad_ID(lookup_obj):
    with pytest.raises(Exception):
        lookup_obj.mlb_id(0)

#!/bin/python

import numpy as np


def test_lookup_AaronHill_by_mlb_ID(lookup_obj):
    s = lookup_obj.from_mlb_ids([431094])
    print(s)
    assert(len(s) == 1)
    assert(s.iloc[0].mlb_name == 'Aaron Hill')


def test_lookup_bad_ID(lookup_obj):
    s = lookup_obj.from_mlb_ids([0])
    assert(len(s) == 0)


def test_lookup_by_mlb_ids(lookup_obj):
    s = lookup_obj.from_mlb_ids([643327, 554430, 621107, 435043])
    print(s)
    assert(len(s) == 4)
    assert(s.iloc[0].mlb_name == 'Zach Duke')
    assert(s.iloc[1].mlb_name == 'Zach Eflin')
    assert(s.iloc[2].mlb_name == 'Zack Godley')
    assert(s.iloc[3].mlb_name == 'Zack Wheeler')


def test_lookup_by_yahoo_ids(lookup_obj):
    s = lookup_obj.from_yahoo_ids([9320, 9449, 9317])
    print(s)
    assert(len(s) == 3)
    assert(s.iloc[0].yahoo_name == 'Chaz Roe')
    assert(s.iloc[1].yahoo_name == 'Christian Yelich')
    assert(s.iloc[2].yahoo_name == 'Hyun-Jin Ryu')


def test_lookup_by_cbs_ids(lookup_obj):
    s = lookup_obj.from_cbs_ids([223481])
    print(s)
    assert(len(s) == 1)
    assert(s.iloc[0].mlb_name == 'Kyle Lohse')
    assert(s.iloc[0].cbs_name == 'Kyle Lohse')
    assert(s.iloc[0].cbs_id == 223481)
    assert(s.iloc[0].mlb_id == 346798)


def test_lookup_by_espn_ids(lookup_obj):
    s = lookup_obj.from_espn_ids([33080])
    print(s)
    assert(len(s) == 1)
    assert(s.iloc[0].mlb_name == 'Adonis Garcia')
    assert(s.iloc[0].espn_id == 33080)
    assert(s.iloc[0].mlb_id == 611177)


def test_lookup_by_fangraphs_ids(lookup_obj):
    s = lookup_obj.from_fangraphs_ids([13677, 'sa739620'])
    print(s)
    assert(len(s) == 2)
    assert(s.iloc[0].mlb_name == 'Corey Oswalt')
    assert(s.iloc[0].fg_id == '13677')
    assert(s.iloc[0].mlb_id == 621261)
    assert(s.iloc[1].mlb_name == 'Thairo Estrada')
    assert(s.iloc[1].fg_id == 'sa739620')
    assert(s.iloc[1].mlb_id == 642731)


def test_lookup_by_name(lookup_obj):
    s = lookup_obj.from_names(['Jose Ramirez'])
    print(s)
    assert(len(s) == 2)
    assert(s.iloc[0].mlb_team == 'ATL')
    assert(s.iloc[0].mlb_pos == 'P')
    assert(s.iloc[1].mlb_team == 'CLE')
    assert(s.iloc[1].mlb_pos == '3B')


def test_lookup_by_name_multi(lookup_obj):
    s = lookup_obj.from_names(['Khris Davis', 'Enrique Hernandez'])
    print(s)
    assert(len(s) == 2)
    assert(s.iloc[0].mlb_name == 'Enrique Hernandez')
    assert(s.iloc[1].ottoneu_name == 'Khristopher Davis')


def test_lookup_by_name_empty(lookup_obj):
    s = lookup_obj.from_names(['Joe Baseball'])
    print(s)
    assert(len(s) == 0)


def test_lookup_by_name_nan_yahoo_id(lookup_obj):
    # In the fake database, A.J. Jimenez has nan for the yahoo ID.  A.J.
    # Pollock has a valid yahoo_ID.
    s = lookup_obj.from_names(['A.J. Jimenez', 'A.J. Pollock'],
                              filter_missing='yahoo_id')
    print(s)
    assert(len(s) == 1)
    assert(np.isnan(s.iloc(0)[0].yahoo_id))
    assert(s.iloc(0)[0].mlb_name == 'A.J. Jimenez')

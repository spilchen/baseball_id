#!/bin/python

"""
APIs to lookup into the baseball map stored at http://crunchtimebaseball.com.

All of the from_* APIs return a DataFrame that has baseball player
particulars for the IDs in the lookup.  For each player that it finds
it will a return row in a panda's DataFrame that has:

>>> Index(['mlb_id', 'mlb_name', 'mlb_pos', 'mlb_team', 'mlb_team_long',
>>>        'bats', 'throws', 'birth_year', 'bp_id', 'bref_id', 'bref_name',
>>>        'cbs_id', 'cbs_name', 'cbs_pos', 'espn_id', 'espn_name', 'espn_pos',
>>>        'fg_id', 'fg_name', 'fg_pos', 'lahman_id', 'nfbc_id', 'nfbc_name',
>>>        'nfbc_pos', 'retro_id', 'retro_name', 'debut', 'yahoo_id',
>>>        'yahoo_name', 'ottoneu_id', 'ottoneu_name', 'ottoneu_pos',
>>>        'rotowire_id', 'rotowire_name', 'rotowire_pos'],
>>>       dtype='object')
"""
import pandas as pd
import numpy as np


class Cache:
    """Class that caches results of baseball ID lookups.

    You can use this to cut down on network traffic if you intend to do many
    calls to the APIs.  The first time we use an API, we'll cache the results
    for subsequent callers.
    """
    def __init__(self, source):
        self.source = source
        self.df = None

    def _read_source(self):
        if self.df is None:
            self.df = pd.read_csv(self.source, encoding='iso-8859-1')

    def from_mlb_ids(self, ids):
        """Lookup given a list of mlb_ID's

        Accepts a list of MLB IDs.  It will return a DataFrame containing
        Series for players that match the MLB IDs passed in.  If nothing was
        found an empty DataFrame is returned.

        :param ids: mlb_ID's to lookup
        :type ids: int list
        :return: Players that match the given IDs.  If none are found an empty
                 DataFrame is returned.
        :rtype: DataFrame

        >>> In [1]: lookup.from_mlb_ids([430945, 607680, 669456])
        >>> Out[1]:
        >>>       mlb_id      mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id rotowire_name  rotowire_pos
        >>> 39    430945    Adam Jones      CF      ARI  ...          OF      8165.0    Adam Jones            OF
        >>> 1746  607680  Kevin Pillar      CF       SF  ...          OF     12678.0  Kevin Pillar            OF
        >>> 2545  669456  Shane Bieber       P      CLE  ...          SP     14383.0  Shane Bieber             P
        >>>
        >>> [3 rows x 35 columns]

        """ # noqa
        self._read_source()
        return self.df[self.df.mlb_id.isin(ids)]

    def from_yahoo_ids(self, ids):
        """Lookup given a list of Yahoo! IDs

        Accepts a list of IDs from Yahoo! fantasy baseball.  It will return a
        DataFrame containing Series for players that match the Yahoo! IDs.  If
        nothing was found an empty DataFrame is returned.

        :param ids: Yahoo! IDs to lookup
        :type ids: int list
        :return: Players that match the given IDs.  If none are found an empty
                 DataFrame is returned.
        :rtype: DataFrame

        >>> In [1]: c.from_yahoo_ids([10794, 9542, 7578])
        >>> Out[1]:
        >>>       mlb_id        mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id   rotowire_name  rotowire_pos
        >>> 5     621345     A.J. Minter       P      ATL  ...          RP     13889.0     A.J. Minter             P
        >>> 204   605151  Archie Bradley       P      ARI  ...          RP     12131.0  Archie Bradley             P
        >>> 2340  448179       Rich Hill       P      LAD  ...          SP      7965.0       Rich Hill             P
        >>>
        >>> [3 rows x 35 columns]

        """ # noqa
        self._read_source()
        return self.df[self.df.yahoo_id.isin(ids)]

    def from_cbs_ids(self, ids):
        """Lookup given a list of CBS IDs

        Accepts a list of IDs from CBS fantasy baseball.  It will return a
        DataFrame containing Series for players that match the IDs.  If nothing
        was found an empty DataFrame is returned.

        :param ids: CBS IDs to lookup
        :type ids: int list
        :return: Players that match the given IDs.  If none are found an empty
                 DataFrame is returned.
        :rtype: DataFrame

        >>> In [1]: lookup.from_cbs_ids([1660162, 2507367])
        >>> Out[1]:
        >>>       mlb_id      mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id rotowire_name  rotowire_pos
        >>> 423   457763  Buster Posey       C       SF  ...        C/1B     10426.0  Buster Posey             C
        >>> 1657  665742     Juan Soto      LF      WSH  ...          OF     13960.0     Juan Soto            OF
        >>>
        >>> [2 rows x 35 columns]

        """ # noqa
        self._read_source()
        return self.df[self.df.cbs_id.isin(ids)]

    def from_espn_ids(self, ids):
        """Lookup given a list of ESPN IDs

        Accepts a list of IDs from ESPN fantasy baseball.  It will return a
        DataFrame containing Series for players that match the IDs.  If nothing
        was found an empty DataFrame is returned.

        :param ids: ESPN IDs to lookup
        :type ids: int list
        :return: Players that match the given IDs.  If no Series are found an
                 empty DataFrame is returned.
        :rtype: DataFrame

        >>> In [1]: c.from_espn_ids([29252])
        >>> Out[1]:
        >>>      mlb_id       mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id  rotowire_name  rotowire_pos
        >>> 836  451594  Dexter Fowler      RF      STL  ...          OF      8271.0  Dexter Fowler            OF
        >>>
        >>> [1 rows x 35 columns]

        """ # noqa
        self._read_source()
        return self.df[self.df.espn_id.isin(ids)]

    def from_fangraphs_ids(self, ids):
        """Lookup given a list of FanGraph IDs

        Accepts a list of IDs as maintained at fangraphs.com.  It will return a
        DataFrame containing Series for players that match the IDs.  If nothing
        was found an empty DataFrame is returned.

        :param ids: FanGraph IDs to lookup
        :type ids: int list
        :return: Players that match the given IDs.  If no Series are found an
                 empty DataFrame is returned.
        :rtype: DataFrame

        >>> In [35]: c.from_fangraphs_ids([19753, 19566])
        >>> Out[35]:
        >>>       mlb_id           mlb_name mlb_pos  ... rotowire_id      rotowire_name rotowire_pos
        >>> 1510  642528  Jonathan Loaisiga       P  ...     15256.0  Jonathan Loaisiga            P
        >>> 2133  663993          Nate Lowe      1B  ...         NaN                NaN          NaN
        >>>
        >>> [2 rows x 35 columns]

        """ # noqa
        self._read_source()
        # The DataFrame for the fangraph ID column is type str.  This is
        # because FanGraph ids can have character values.  Convert all of
        # the input IDs to strings so that it finds the all numeric ones.
        ids_as_str = [str(i) for i in ids]
        return self.df[self.df.fg_id.isin(ids_as_str)]

    def from_names(self, names, filter_missing=None):
        """Lookup given a list of player names

        Accepts a list of player names.  The names must match exactly.  It will
        return a DataFrame containing tuples for each player name that matches.

        An optional argument exists to filter based on names and those that
        have a missing field.  See explanation of the filter_missing parameter.

        :param names: Player names to lookup
        :type str: str list
        :param filter_missing: Optional parameter that allows for additional
           filtering.  Only players that have this field name missing (Nan)
           will be returned.  This is useful for use with one of the other ID
           based lookup where the ID may not be in the database.  For example,
           set this to 'yahoo_id' to lookup of a rookie who doesn't yet have a
           yahoo_id in the database.
        :type filter_missing: str
        :return: Players that match the given names.  If no Series are found an
            empty DataFrame is returned.
        :rtype: DataFrame

        >>> In [28]: lk.from_names(['Khris Davis', 'Enrique Hernandez'])
        >>> Out[28]:
        >>>       mlb_id           mlb_name mlb_pos mlb_team        mlb_team_long  ...       ottoneu_name  ottoneu_pos  rotowire_id      rotowire_name rotowire_pos
        >>>       966   571771  Enrique Hernandez      CF      LAD  Los Angeles Dodgers  ...  Enrique Hernandez  1B/2B/SS/OF      11139.0  Enrique Hernandez           SS
        >>>       1753  501981        Khris Davis      LF      OAK    Oakland Athletics  ...  Khristopher Davis           OF      11664.0        Khris Davis           OF
        >>>
        >>> [2 rows x 35 columns]
        """ # noqa
        self._read_source()
        flt = (self.df.mlb_name.isin(names)) | \
            (self.df.bref_name.isin(names)) | \
            (self.df.cbs_name.isin(names)) | \
            (self.df.espn_name.isin(names)) | \
            (self.df.fg_name.isin(names)) | \
            (self.df.retro_name.isin(names)) | \
            (self.df.yahoo_name.isin(names)) | \
            (self.df.ottoneu_name.isin(names)) | \
            (self.df.rotowire_name.isin(names))
        if filter_missing is not None:
            flt &= (np.isnan(self.df[filter_missing]))
        return self.df[flt]

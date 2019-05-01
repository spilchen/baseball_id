#!/bin/python

import pandas as pd


class Lookup:
    """Class that manages lookup of baseball players by various IDs.

    All of the from_* APIs return a DataFrame that has baseball player
    particulars for the IDs in the lookup.  For each player that it finds
    it will a row in a panda's DataFrame that has:
    - birth year
    - bat handed, throw handed
    - from various databases (e.g. MLB, baseball-reference.com, Yahoo!, ESPN,
      CBS, etc.)
      - name
      - position in various databases
      - ID
    """
    def __init__(self):
        self.source = 'http://crunchtimebaseball.com/master.csv'
        self.df = None
        pass

    def set_source(self, source):
        self.source = source

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
        """
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
        """
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
        """
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
        """
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
        """
        self._read_source()
        # The DataFrame for the fangraph ID column is type str.  This is
        # because FanGraph ids can have character values.  Convert all of
        # the input IDs to strings so that it finds the all numeric ones.
        ids_as_str = [str(i) for i in ids]
        return self.df[self.df.fg_id.isin(ids_as_str)]

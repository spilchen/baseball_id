#!/bin/python

import pandas as pd


class Lookup:
    def __init__(self):
        self.source = 'http://crunchtimebaseball.com/master.csv'
        self.df = None
        pass

    def set_source(self, source):
        self.source = source

    def _read_source(self):
        if self.df is None:
            self.df = pd.read_csv(self.source, encoding='iso-8859-1')

    def mlb_id(self, id):
        """Lookup the given mlb_ID

        :param id: mlb_ID to lookup
        :type id: int
        :return: Particulars of the given mlb_ID lookup
        :rtype: Series
        """
        self._read_source()
        lookup_df = self.df[self.df.mlb_id == id]
        if lookup_df.size == 0:
            raise KeyError("Could not player for mlb_ID {}".format(id))
        return lookup_df.iloc[0]

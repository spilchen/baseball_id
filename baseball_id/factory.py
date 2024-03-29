#!/bin/python

from baseball_id import lookup
import importlib.resources as pkg_resources
import ssl


class Factory:
    """Factory methods to construct the ID lookup cache object."""
    @classmethod
    def create(cls):
        """Factory method to create a cache object from github/spilchen/baseball_id_db

        This is called as part of package initialization and so can be refered
        to via the Lookup variable.

        >>> from baseball_id import Lookup
        >>> Lookup.from_yahoo_ids([10794, 9542, 7578])
        """
        ssl._create_default_https_context = ssl._create_unverified_context
        c = lookup.Cache('https://raw.githubusercontent.com/spilchen/baseball_id_db/main/master.csv')
        return c

    @classmethod
    def create_fake(cls):
        """Factory method to create a fake data source

        This refers to a static data file that is in the current package.  This
        function exists for testing purposes as it avoids network traffic to
        get the actual up-to-date ID mapping.
        """
        source = pkg_resources.open_text('baseball_id', 'sample.master.csv',
                                         encoding='iso-8859-1')
        c = lookup.Cache(source)
        return c

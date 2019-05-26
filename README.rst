===========
baseball_id
===========

Do you analyze baseball data from several sources and need to find a way to correlate it for the same player?  The owners at https://crunchtimebaseball.com publish a map_ for this purpose.  With the map you can take a player from Yahoo! and cross reference with data from sites such as http://baseball-reference.com, http://fangraphs.com, http://www.seanlahman.com.  This package gives you a way to access this map within Python.  A set of APIs allow you to do lookup of players by a variety of different IDs.

.. _map: http://crunchtimebaseball.com/baseball_map.html

Build status
------------

.. image:: https://travis-ci.com/spilchen/baseball_id.svg?branch=master
    :target: https://travis-ci.com/spilchen/baseball_id
    
.. image:: https://readthedocs.org/projects/baseball-id/badge/?version=latest
    :target: https://baseball-id.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Installation
------------

This package can be installed via pip:

::

  pip install baseball_id


or from the repo:

::

  git clone https://github.com/spilchen/baseball_id
  cd baseball_id
  python setup.py install

Documentation
-------------

The documentation are hosted at readthedocs.io: https://baseball-id.readthedocs.io/en/latest/

Sample API Usage
----------------

::

  In [1]: from baseball_id import Lookup

  In [2]: Lookup.from_mlb_ids([430945, 607680, 669456])
  Out[2]:
        mlb_id      mlb_name mlb_pos mlb_team         mlb_team_long  ...  ottoneu_name ottoneu_pos  rotowire_id  rotowire_name rotowire_pos
  39    430945    Adam Jones      CF      ARI  Arizona Diamondbacks  ...    Adam Jones          OF       8165.0     Adam Jones           OF
  1746  607680  Kevin Pillar      CF       SF  San Francisco Giants  ...  Kevin Pillar          OF      12678.0   Kevin Pillar           OF
  2545  669456  Shane Bieber       P      CLE     Cleveland Indians  ...  Shane Bieber          SP      14383.0   Shane Bieber            P
  
  [3 rows x 35 columns]
  
  In [3]: Lookup.from_yahoo_ids([10794, 9542, 7578])
  Out[3]:
        mlb_id        mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id   rotowire_name  rotowire_pos
  5     621345     A.J. Minter       P      ATL  ...          RP     13889.0     A.J. Minter             P
  204   605151  Archie Bradley       P      ARI  ...          RP     12131.0  Archie Bradley             P
  2340  448179       Rich Hill       P      LAD  ...          SP      7965.0       Rich Hill             P
  
  [3 rows x 35 columns]
  
  In [4]: Lookup.from_cbs_ids([1660162, 2507367])
  Out[4]:
        mlb_id      mlb_name mlb_pos mlb_team         mlb_team_long  ...  ottoneu_name ottoneu_pos  rotowire_id  rotowire_name rotowire_pos
  423   457763  Buster Posey       C       SF  San Francisco Giants  ...  Buster Posey        C/1B      10426.0   Buster Posey            C
  1657  665742     Juan Soto      LF      WSH  Washington Nationals  ...     Juan Soto          OF      13960.0      Juan Soto           OF
  
  [2 rows x 35 columns]
  
  In [5]: Lookup.from_espn_ids([29252])
  Out[5]:
       mlb_id       mlb_name mlb_pos mlb_team        mlb_team_long  ...   ottoneu_name ottoneu_pos  rotowire_id  rotowire_name rotowire_pos
  836  451594  Dexter Fowler      RF      STL  St. Louis Cardinals  ...  Dexter Fowler          OF       8271.0  Dexter Fowler           OF
  
  [1 rows x 35 columns]
  
  In [6]: Lookup.from_fangraphs_ids([19753, 19566])
  Out[6]:
        mlb_id           mlb_name mlb_pos mlb_team  ... ottoneu_pos rotowire_id      rotowire_name  rotowire_pos
  1510  642528  Jonathan Loaisiga       P      NYY  ...       SP/RP     15256.0  Jonathan Loaisiga             P
  2133  663993          Nate Lowe      1B       TB  ...          1B         NaN                NaN           NaN
  
  [2 rows x 35 columns]

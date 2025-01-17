"""An unofficial Python wrapper for the Binance exchange API v3

.. moduleauthor:: Sam McHardy

"""

__version__ = '0.6.8'

from binance.client import Client  # noqa
from binance.client_async import AsyncClient # noqa
from binance.depthcache import DepthCacheManager  # noqa
from binance.websockets import BinanceSocketManager  # noqa

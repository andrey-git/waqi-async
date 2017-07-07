"""asyncio-friendly python API for waqi (https://aqicn.com)."""
import asyncio
import aiohttp
import async_timeout

BASE_URL = 'https://api.waqi.info/'
SEARCH_URL = BASE_URL + 'search/'
FEED_NAME_URL = BASE_URL + 'feed/{}/'
FEED_NUMBER_URL = BASE_URL + 'feed/@{}/'


class WaqiClient(object):
    """Waqi client implementation."""

    def __init__(self, token, session=None,
                 timeout=aiohttp.client.DEFAULT_TIMEOUT):
        """Constructor.

        token: Token from http://aqicn.org/data-platform/token/#/
        session: aiohttp.ClientSession or None to create a new session.
        """
        self._params = {'token': token}
        self._timeout = timeout
        if session is not None:
            self._session = session
        else:
            self._session = aiohttp.ClientSession()

    @asyncio.coroutine
    def search(self, keyword):
        """Search for a station/location by name."""
        return (yield from self._get(SEARCH_URL, keyword=keyword))

    @asyncio.coroutine
    def get_station_by_name(self, name):
        """Get data by station name."""
        return (yield from self._get(FEED_NAME_URL.format(name)))

    @asyncio.coroutine
    def get_station_by_number(self, number):
        """Get data by station number."""
        return (yield from self._get(FEED_NUMBER_URL.format(number)))

    @asyncio.coroutine
    def _get(self, path, **kwargs):
        with async_timeout.timeout(self._timeout):
            resp = yield from self._session.get(
                path, params=dict(self._params, **kwargs))
            return (yield from resp.json())['data']

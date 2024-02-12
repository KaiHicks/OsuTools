import requests
from urllib.parse import urljoin, urlunsplit
import logging

log = logging.getLogger(__name__)


class ChimuClient:
    def __init__(self, endpoint: str):
        self._endpoint = endpoint

    def download_betmapset(self, beatmapset_id: str) -> bytes:
        url = urljoin(self._endpoint, f"download/{beatmapset_id}")
        log.debug(f"Getting beatmap with url: {url}")
        response = requests.get(url)
        log.debug(f"Got response: {[key for key in response.__dict__]=}")

        return response.content

import logging
from ossapi import Ossapi
from ossapi.enums import UserLookupKey, UserBeatmapType
from ossapi.models import BeatmapsetCompact
from osutools.facade.chimuclient import ChimuClient
from typing import Set
import tempfile
from pathlib import Path

log = logging.getLogger(__name__)

# This is what osu.ppy.sh uses
BEATMAP_PAGE_SIZE = 51
# https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names
ILLEGAL_FILE_PATH_CHARS_TRANSLATION = str.maketrans(
    '<>:"/\\|?&*', '----------'
)


class DownloaderHandler:
    def __init__(self, osu_client: Ossapi, chimu_client: ChimuClient):
        self._osu_client = osu_client
        self._chimu_client = chimu_client

        self._downloaded_beatmapset_ids: Set[str] = set()

    def run(
        self, download_dir: str, username: str, num_songs: int, offset: int
    ) -> None:
        log.info(
            f"Downloading {num_songs} recently played songs of user {username} starting"
            f" at page {offset}"
        )

        target_user = self._osu_client.user(username, key=UserLookupKey.USERNAME)
        user_id = target_user.id

        num_downloaded = 0
        while num_downloaded < num_songs or num_songs == -1:
            beatmaps_page = self._osu_client.user_beatmaps(
                user_id,
                UserBeatmapType.MOST_PLAYED,
                limit=BEATMAP_PAGE_SIZE,
                offset=num_downloaded+offset,
            )
            if not beatmaps_page:
                break

            for beatmap_playcount in beatmaps_page:
                self._handle_beatmap(download_dir, beatmap_playcount.beatmapset)

            num_downloaded += len(beatmaps_page)
            log.info(
                f"Downloaded {num_downloaded} /"
                f" {num_songs} [{num_downloaded/num_songs*100:.1f}]"
            )

    def _handle_beatmap(self, download_dir: str, beatmapset: BeatmapsetCompact):
        if beatmapset.id in self._downloaded_beatmapset_ids:
            log.info(f"Already downloaded {beatmapset.title}")
            return

        log.info(f"Downloading {beatmapset.title} by {beatmapset.artist}")
        log.debug(f"Got beatmapset: {beatmapset}")
        self._write_beatmap(download_dir, beatmapset)

        self._downloaded_beatmapset_ids.add(beatmapset.id)

    def _write_beatmap(self, download_dir: str, beatmapset: BeatmapsetCompact):
        download_bytes = self._chimu_client.download_betmapset(str(beatmapset.id))

        # Using file name scheme from osu.ppy.sh
        filename = f"{beatmapset.id} {beatmapset.artist} - {beatmapset.title}.osz"
        filename_safe = filename.translate(ILLEGAL_FILE_PATH_CHARS_TRANSLATION)
        with open(Path(download_dir) / Path(filename_safe), "wb") as f:
            f.write(download_bytes)

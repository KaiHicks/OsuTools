import argparse
from osutools.downloader.downloaderhandler import DownloaderHandler
from ossapi import Ossapi
from osutools.facade.chimuclient import ChimuClient


def build_downloader_handler():
    arg_parser = provide_arg_parser()


def provide_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osutools", description="A collection of scripts for the game Osu"
    )
    parser.add_argument(
        "downloaddir",
        help=(
            "Directory to download songs to. If you make this your Osu songs directory,"
            " Osu will automatically import the songs and delete the download files."
        ),
    )
    parser.add_argument(
        "username", help="Username of the user whose songs you want to download"
    )
    parser.add_argument(
        "-n",
        default=-1,
        help="Number of songs to download. Default -1 (unlimited)",
        type=int,
    )
    parser.add_argument("-i", default=0, help="Page offset. Default 0", type=int)

    return parser


def provide_downloader_handler(
    osu_client: Ossapi, chimu_client: ChimuClient
) -> DownloaderHandler:
    return DownloaderHandler(osu_client, chimu_client)

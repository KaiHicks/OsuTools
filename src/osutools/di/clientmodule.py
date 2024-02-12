from __future__ import annotations
from ossapi import Ossapi
from dataclasses import dataclass
from os import environ
from osutools.facade.chimuclient import ChimuClient

# --- Osu ---


def provide_osu_client(osu_credentials: OsuCredentials) -> Ossapi:
    return Ossapi(*osu_credentials)


def provide_client_credentials() -> OsuCredentials:
    # Pull credentials from environment variables
    # TODO: Onboard to browser-based authentication
    return OsuCredentials(
        client_id=environ.get("OSU_CLIENT_ID"),
        client_secret=environ.get("OSU_CLIENT_SECRET"),
    )


@dataclass
class OsuCredentials:
    client_id: str
    client_secret: str

    def __iter__(self):
        return iter((self.client_id, self.client_secret))


# --- Chimu ---
CHIMU_ENDPOINT = "https://api.chimu.moe/v1/"


def provide_chimu_client() -> ChimuClient:
    return ChimuClient(CHIMU_ENDPOINT)

# OsuTools

OsuTools is a collection of osu scripts. At the moment, there is only the song downloader which downloads songs played by a particular user by username.

## Setup

With Python (recommended 3.11 or newer) install PipEnv with

```
python3 -m pip install pipenv
```

Then, use PipEnv to install all required dependencies

```
python3 -m pipenv install
```

## Usage

To run the song downloader:
```
python3 -m pipenv run song-downloader [-h] [-n N] [-i I] downloaddir username

positional arguments:
  downloaddir  Directory to download songs to. If you make this your Osu songs directory, Osu will automatically import the songs and delete the download files.
  username     Username of the user whose songs you want to download

options:
  -h, --help   show this help message and exit
  -n N         Number of songs to download. Default -1 (unlimited)
  -i I         Page offset. Default 0
```


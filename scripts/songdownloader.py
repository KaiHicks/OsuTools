from osutools.di import songdownloadermodule, clientmodule
import logging


def main():
    osu_client = clientmodule.provide_osu_client(
        clientmodule.provide_client_credentials()
    )
    chimu_client = clientmodule.provide_chimu_client()
    handler = songdownloadermodule.provide_downloader_handler(osu_client, chimu_client)
    arg_parser = songdownloadermodule.provide_arg_parser()

    args = arg_parser.parse_args()
    handler.run(args.downloaddir, args.username, args.n, args.i)


if __name__ == "__main__":
    main()

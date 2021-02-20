import os
import random

from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

import config


def main():
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        def job():
            print("Changing profile picture...", end="")
            client(UploadProfilePhotoRequest(
                file=client.upload_file(config.dir + random.choice(os.listdir(config.dir)))
            ))
            client(DeletePhotosRequest([client.get_profile_photos('me')[1]]))
            print("Done!")

        job()


if __name__ == '__main__':
    main()

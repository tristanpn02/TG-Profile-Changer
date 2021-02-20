import os
import random
import time
import schedule

from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

import config


def main():
    with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        def job():
            image = config.dir + random.choice(os.listdir(config.dir))
            print("Changing profile picture to", image + "...", end="")
            client(UploadProfilePhotoRequest(
                file=client.upload_file(image)
            ))
            client(DeletePhotosRequest([client.get_profile_photos('me')[1]]))
            print("Done!")

        schedule.every().day.at("00:00").do(job)

        while True:
            schedule.run_pending()
            time.sleep(60)


if __name__ == '__main__':
    main()

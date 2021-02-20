# TG-Profile-Changer
Changes your Telegram user profile picture randomly every single day

## Installation
For basic installation, you'll need `Python3.x`

You can install the required packages manually listed in `requirements.txt` using ```pip install <library>``` or automatically by ```pip install -r requirements.txt```.

You will have to modify `config.py` with your `api_id` and `api_hash` to login to Telegram, you can find these at https://my.telegram.org/auth. If you'd like, you can also change the `session_name` (*login without auth*) and `dir` (*directory of your images*).

Finally, just slap some images into the directory specified by `dir` in `config.py`!

## Running
You can run the program manually using ```python main.py``` or if you wish to change your profile picture immediately, you can use ```python now.py``` (I know, it's a pretty lazy method X3)

**Before setting up automation** (systemd, crontab etc.), you will have to run the code manually with ```python main.py``` and log in using authentication (*input your phone number, put in auth code*) and **make sure that your working directory is set to the repository** otherwise the program will not use your login session or load your pictures from the specified directory if full directory path is not given.

#### Feel free to modify to your liking and cheers for in advance!

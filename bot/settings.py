"""Constants for the bot."""

import os
from pathlib import Path

TOKEN = os.environ.get("FRIENDO_TOKEN")

MEME_USERNAME = os.environ.get("MEME_USERNAME")

MEME_PASSWORD = os.environ.get("MEME_PASSWORD")

# event api key
EVENT_API_KEY = os.environ.get("EVENT_API_KEY")

WEATHER_TOKEN = os.environ.get("WEATHER_TOKEN")

COMMAND_PREFIX = "."

VERSION = "1.2."

NAME = "Friendo"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMG_CACHE = Path(BASE_DIR, "image_cache")

BASE_GITHUB_REPO = "https://github.com/fisher60/Friendo_Bot"

<<<<<<< develop

LOG_FILE_NAME = "friendo.log"
=======
LOG_FILE_PATH = Path(BASE_DIR, "logs")
>>>>>>> develop

API_COGS = ["events", "memes"]

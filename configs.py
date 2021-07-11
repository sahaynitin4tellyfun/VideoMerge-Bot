# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
**Hello {}, I'm a Simple Video Merger Bot!
I can Merge Multiple Videos into One Video, Generate ScreenShots, Generate Sample Video and many extra features....!

Configure The Settings Before using meh...!
Check Below Buttons for more..! 

🤖 Developer : [Animesh Verma](https://t.me/Animesh941)**
"""
    ABOUT_TEXT = """
**● Developed By : [This Person](https://t.me/Animesh941)
● Updates Channel : [A𝕍Botz](https://t.me/AVBotz)
● Support : [A𝕍Botz Support](https://t.me/AVBotz_Support)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @AVBotz ❤️**
"""

    HELP_TEXT = """**Hello {}, It's too easy to use me..**
 
**● Configure the Settings before using me... 
● Send a photo to set it as your custom thumbnail...
● Send any File or media you want to rename... 
● That's it, and rest is mine work... 

📝 Available Commands... 
- /start - Start the Bot
- /help - This Message
- /about - About Meh
- /settings - Configure Settings 
- /showthumb & /deletethumb - For Thumbnail

© By @AVBotz ❤️**
"""
    
    CAPTION = "**__© Merged By @AVBotz ❤️__**"
    PROGRESS = """
**Percentage : {0}%**
**Done: {1}**
**Total: {2}**
**Speed: {3}/s**
**ETA: {4}**
"""

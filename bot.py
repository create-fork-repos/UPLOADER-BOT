#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR

import os
from config import Config
from pyrogram import Client as Clinton

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@UPLOADER_X_BOT",
    bot_token="6186365167:AAF8ApYrxjvm-oR0I6CZE_OHyrki9a1RMVw",
    api_id=3704772,
    api_hash="b8e50a035abb851c0dd424e14cac4c06",
    plugins=plugins)
    Warrior.run()

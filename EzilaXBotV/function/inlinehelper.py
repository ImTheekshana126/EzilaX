
# Ported from https://github.com/TheHamkerCat/WilliamButcherBot
"""
MIT License
Copyright (c) 2021 TheHamkerCat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import sys
from random import randint
from time import time

import aiohttp
from aiohttp import ClientSession
from googletrans import Translator
from motor import version as mongover
from pykeyboard import InlineKeyboard
from pyrogram import __version__ as pyrover
from pyrogram.raw.functions import Ping
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
from Python_ARQ import ARQ
from search_engine_parser import GoogleSearch

from EzilaXBotV import BOT_USERNAME, OWNER_ID
from EzilaXBotV.conf import get_str_key
from EzilaXBotV.function.pluginhelpers import convert_seconds_to_minutes as time_convert

import asyncio
import math
import shlex
import sys
import time
import traceback
from functools import wraps
from typing import Callable, Coroutine, Dict, List, Tuple, Union

import aiohttp
from PIL import Image
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User

from EzilaXBotV import OWNER_ID, SUPPORT_CHAT
from EzilaXBotV import pbot


def get_user(message: Message, text: str) -> [int, str, None]:
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1

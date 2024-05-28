from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text=_["S_B_11"],
                url=f"https://telegra.ph/SANKI-XD-MUSIC-05-27",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_10"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_13"], user_id=config.HANDLER_ID),
            InlineKeyboardButton(
                text=_["S_B_12"],
                url=f"https://t.me/SANKI_XDX",
            )
        ],   
    ]
    ]
    return buttons

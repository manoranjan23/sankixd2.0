from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app

# stream_markup function jo play, pause, stop aur skip buttons banata hai
def stream_markup(_):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["PLAY_BUTTON"], callback_data="play_callback"),
                InlineKeyboardButton(text=_["PAUSE_BUTTON"], callback_data="pause_callback"),
            ],
            [
                InlineKeyboardButton(text=_["STOP_BUTTON"], callback_data="stop_callback"),
                InlineKeyboardButton(text=_["SKIP_BUTTON"], callback_data="skip_callback"),
            ],
        ]
    )
    return buttons

# stream_markup_timer function jo timer se related buttons banata hai
def stream_markup_timer(_):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["PAUSE_TIMER"], callback_data="pause_timer_callback"),
                InlineKeyboardButton(text=_["RESUME_TIMER"], callback_data="resume_timer_callback"),
            ],
            [
                InlineKeyboardButton(text=_["STOP_TIMER"], callback_data="stop_timer_callback"),
                InlineKeyboardButton(text=_["RESTART_TIMER"], callback_data="restart_timer_callback"),
            ],
        ]
    )
    return buttons

# Help panel ka function
def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data="mbot_cb",
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data="mbot_cb",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                ),
            ],
            mark,
        ]
    )
    return upl

# Help back ka function
def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                ),
            ]
        ]
    )
    return upl

# Private help panel ka function
def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# BUTTONS ka basic structure
BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Play", callback_data="play_callback")],
        [InlineKeyboardButton("Pause", callback_data="pause_callback")],
        [InlineKeyboardButton("Stop", callback_data="stop_callback")],
        [InlineKeyboardButton("Skip", callback_data="skip_callback")],
    ]
)
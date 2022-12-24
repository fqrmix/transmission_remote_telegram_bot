
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Music",
            callback_data="set-category_music"
        ),
        InlineKeyboardButton(
            text="Movies",
            callback_data="set-category_movie"
        ),
        InlineKeyboardButton(
            text="TV Shows",
            callback_data="set-category_tvshow"
        ),
        InlineKeyboardButton(
            text="Download",
            callback_data="start_download"
        )
    )
    return builder.as_markup()
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from keyboards.category import get_inline_kb
from .middleware import TorrentMiddleware

router = Router()
torrent_middleware = TorrentMiddleware()
router.message.middleware(torrent_middleware)
router.callback_query.middleware(torrent_middleware)


@router.message(content_types="text")
async def handle_message(message: Message, torrent_object, error):
    if error:
        await message.answer(
            text=f'Middleware error!\n{error}'
        )
    else:
        await message.answer(
            text=f'Torrent was successfully parsed\n'\
                f'Torrent type: {torrent_object.type}\n'\
                f'Category: {torrent_object.category}\n'\
                f'If you want to change category of torrent - choose option in menu below and press "Download".',
            reply_markup=get_inline_kb()
        )

@router.callback_query(lambda callback: callback.data.startswith('set-category_'))
async def handle_category_callback(callback: CallbackQuery, torrent_object):
    await callback.message.edit_text(
        text=f'Category was changed\n'\
            f'Torrent type: {torrent_object.type}\n'\
            f'Category: {torrent_object.category}\n'\
            f'If you want to change category of torrent - choose option in menu below and press "Download".',
        reply_markup=get_inline_kb()
    )
        

@router.callback_query(lambda callback: callback.data == 'start_download')
async def handle_download_callback(callback: CallbackQuery, torrent_list):
    await callback.message.answer(
        text=f'Download has started\n'
            f'{torrent_list}'
    )

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from transmission_remote_core.src import transmission_controller

router = Router()

@router.message(content_types="text")
async def handle_message(message: Message):

    response = transmission_controller.add_torrent(message.text)
    print(response)
    if response:
        await message.answer(text='Torrent added')
    else:
        await message.answer(text='Torrent not added')


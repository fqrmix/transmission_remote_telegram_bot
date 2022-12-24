from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from transmission_remote_core.app import TransmissionFacade
from typing import Callable, Dict, Any, Awaitable

class TorrentMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.torrent_object = None

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        print(type(event))
        data['torrent_object'] = self.torrent_object
        if type(event) is Message:
            print('Message')
            transmission_facade = TransmissionFacade()
            self.torrent_object = transmission_facade.get_torrent_object(data['event_update'].message.text)
            data['torrent_object'] = self.torrent_object
            return await handler(event, data)
        
        if type(event) is CallbackQuery:
            return await handler(event, data)



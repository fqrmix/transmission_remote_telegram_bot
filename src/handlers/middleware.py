from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from transmission_remote_core.app import TransmissionFacade
from transmission_remote_core.app.core.controller.exception import ParseErorr
from typing import Callable, Dict, Any, Awaitable

transmission_facade = TransmissionFacade()

class TorrentMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.torrent_object = None
        self.torrent_list = None
        self.error = None

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        data['torrent_object'] = self.torrent_object
        data['torrent_list'] = self.torrent_list
        data['error'] = self.error

        if type(event) is Message:
            try:
                message = data['event_update'].message
                self.torrent_object = transmission_facade.get_torrent_object(message.text)
                data['torrent_object'] = self.torrent_object
                return await handler(event, data)
            except Exception as error:
                print('Middleware error')
                print(error)
                self.error = error
                data['error'] = self.error
                return await handler(event, data)
            finally:
                self.error = None
        
        if type(event) is CallbackQuery:
            if data['event_update'].callback_query.data.startswith('set-category_'):
                category = data['event_update'].callback_query.data.replace('set-category_', '')
                transmission_facade.change_category(self.torrent_object, category)
                return await handler(event, data)
    
            if data['event_update'].callback_query.data == 'start_download':
                transmission_facade.add_torrent(self.torrent_object)
                self.torent_list = transmission_facade.get_torrent_list()
                data['torrent_list'] = self.torrent_list
                return await handler(event, data)



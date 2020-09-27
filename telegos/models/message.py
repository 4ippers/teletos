#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.models.base import BaseModel
from telegos.models.user import UserModel


class MessageModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.chat_id = None
        self.message_id = None

        self.audio = None
        self.caption = None
        self.photo = None
        self.text = None

        self.contact = None
        self.location = None

        self.from_user = None
        self.reply_to_message = None

        self._dict_handlers = {
            "from_user": UserModel,
            "reply_to_message": MessageModel,
        }

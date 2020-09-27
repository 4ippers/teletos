#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.models.base import BaseModel
from telegos.models.user import UserModel
from telegos.models.message import MessageModel


class CallBackQueryModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.id = None
        self.chat_instance = None
        self.data = None
        self.from_user = None
        self.inline_message_id = None
        self.message = None

        self._dict_handlers = {
            "from_user": UserModel,
            "message": MessageModel,
        }
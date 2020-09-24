#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.models.base import BaseModel
from telegos.models.user import UserModel


class MessageModel(BaseModel):
    def __init__(self):
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

        self._handler = {
            "from_user": UserModel,
            "reply_to_message": MessageModel,
        }

    def from_tg(self, data):
        class_vars = self.__dict__
        for var in class_vars:
            if var.startswith("_"):
                continue

            if atr := getattr(data, var):
                if var in self._handler:
                    model = self._handler[var]()
                    model.from_tg(atr)
                    atr = model.to_dict()
                setattr(self, var, atr)
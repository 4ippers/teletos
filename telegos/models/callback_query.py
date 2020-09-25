#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.models.base import BaseModel
from telegos.models.user import UserModel
from telegos.models.message import MessageModel


class CallBackQueryModel(BaseModel):
    def __init__(self):
        self.id = None
        self.chat_instance = None
        self.data = None
        self.from_user = None
        self.inline_message_id = None
        self.message = None

        self._handler = {
            "from_user": UserModel,
            "message": MessageModel,
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
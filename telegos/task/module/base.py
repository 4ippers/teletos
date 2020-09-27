#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.task.base import BaseTask


class ModuleTaskTypes:
    SEND_MESSAGE = "send_message"
    EDIT_MESSAGE = "edit_message"
    DELETE_MESSAGE = "delete_message"
    SEND_PHOTO = "send_photo"


class ModuleTaskBase(BaseTask):
    def __init__(self, module_name):
        super().__init__()
        self.module = module_name
        self.reply_markup = None
        self.reply_to_message_id = None
        self.type = None

    def check(self):
        pass


class ModuleTaskBaseChatIdPhone(ModuleTaskBase):
    def __init__(self, module_name: str, chat_id: str = None, phone: str = None):
        super().__init__(module_name=module_name)
        self.chat_id = chat_id
        self.phone = phone

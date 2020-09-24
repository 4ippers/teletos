#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from models.parse_mode import ParseMode
from .base import MessageBaseChatIdPhone, ModuleTaskTypes


class MessageText(MessageBaseChatIdPhone):
    TYPE_NAME = ModuleTaskTypes.SEND_MESSAGE

    def __init__(self, module_name: str, text: str, parse_mode: str = ""):
        super().__init__(module_name)
        self.type = self.TYPE_NAME
        self.text = text
        self.parse_mode = parse_mode if parse_mode else ParseMode.MARKDOWN


class DeleteMessage(MessageBaseChatIdPhone):
    TYPE_NAME = ModuleTaskTypes.DELETE_MESSAGE

    def __init__(self, module_name: str, message_id: str):
        super().__init__(module_name=module_name)
        self.type = self.TYPE_NAME
        self.message_id = message_id

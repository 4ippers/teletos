#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.task.core.core import CoreTask, CoreTaskTypes
from telegos.models.message import MessageModel


class CoreTaskMessage(CoreTask):
    TYPE_NAME = CoreTaskTypes.MESSAGE

    def __init__(self, to_module: str, chat_id: str, message: MessageModel):
        super().__init__(to_module, chat_id=chat_id)
        self.type = self.TYPE_NAME
        self.message = message.to_dict()

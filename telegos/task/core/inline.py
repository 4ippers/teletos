#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.task.core.core import CoreTask, CoreTaskTypes
from telegos.models.callback_query import CallBackQueryModel


class CoreTaskInlineButton(CoreTask):
    TYPE_NAME = CoreTaskTypes.INLINE_BUTTON

    def __init__(self, to_module: str, chat_id: str, callback: CallBackQueryModel):
        super().__init__(to_module, chat_id=chat_id)
        self.type = self.TYPE_NAME
        self.callback: CallBackQueryModel = callback

        self._dict_handlers = {
            'callback': CallBackQueryModel
        }
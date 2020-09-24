#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .core import CoreTask, CoreTaskTypes


class CoreTaskInit(CoreTask):
    TYPE_NAME = CoreTaskTypes.INIT

    def __init__(self, to_module: str, chat_id: str):
        super().__init__(to_module, chat_id=chat_id)
        self.type = self.TYPE_NAME


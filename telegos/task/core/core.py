#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from task.base import BaseTask


class CoreTaskTypes:
    INIT = "init"
    MESSAGE = "message"


class CoreTask(BaseTask):
    def __init__(self, to_module: str, chat_id: str):
        super().__init__()
        self.chat_id = chat_id
        self.module = to_module
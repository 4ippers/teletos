#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.task.module.base import ModuleTaskBaseChatIdPhone, ModuleTaskTypes


class ModuleTaskSendPhoto(ModuleTaskBaseChatIdPhone):
    TYPE_NAME = ModuleTaskTypes.SEND_PHOTO

    def __init__(self, module_name: str, photo_path: str):
        super(ModuleTaskSendPhoto, self).__init__(module_name=module_name)
        self.type = self.TYPE_NAME
        self.photo = photo_path
        self.caption = None
        self.parse_mode = None
        self.disable_notification = None


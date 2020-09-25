#!/usr/bin/env python
# -*- coding: utf-8 -*-


class KeyboardButton:
    JOIN_SYMBOL = ";"

    def __init__(self, text: str):
        self.text = text

    def to_dict(self):
        keys = ""
        if self.text:
            keys = f"{self.text}{self.JOIN_SYMBOL}"
        return keys


class InlineKeyButton:
    JOIN_SYMBOL = "|"

    def __init__(self, module_name: str, text: str, callback_data: str, url=None):
        self.text = text
        self.callback_data = f"{module_name}{self.JOIN_SYMBOL}{callback_data}"
        self.url = url
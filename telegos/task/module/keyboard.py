#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from telegos.helpers.dict_helper import DictSerialize


class ButtonTypes:
    INLINE = "inline_button"
    KEYBOARD = "keyboard_button"


class Button(DictSerialize):
    JOIN_SYMBOL = ""

    def __init__(self):
        super().__init__()
        self.type = None


class KeyButton(Button):
    JOIN_SYMBOL = ""

    def __init__(self, text: str):
        super().__init__()
        self.type = ButtonTypes.KEYBOARD
        self.text = text


class InlineKeyButton(Button):
    JOIN_SYMBOL = "|"

    def __init__(self, module_name: str, text: str, callback_data: str, url=None):
        super().__init__()
        self.type = ButtonTypes.INLINE
        self.text = text
        self.callback_data = f"{module_name}{self.JOIN_SYMBOL}{callback_data}"
        self.url = url
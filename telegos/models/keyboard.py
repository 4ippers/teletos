#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

`class ButtonTypes:
    INLINE = "inline_button"
    KEYBOARD = "keyboard_button"


class Button:
    _JOIN_SYMBOL = ""

    def __init__(self):
        self.type = None

    def to_dict(self, pass_null=True, pass_internal_attr=True):
        result = {}
        for var in self.__dict__:
            if pass_internal_attr and var.startswith("_"):
                continue

            if not pass_null:
                result[var] = self.__dict__[var]
                continue

            if self.__dict__[var]:
                result[var] = self.__dict__[var]
        return result

    def from_dict(self, dict_data: dict):
        keys = self.__dict__.keys()
        for key, value in dict_data.items():
            if key in keys:
                setattr(self, key, value)


class KeyButton(Button):
    _JOIN_SYMBOL = ";"

    def __init__(self, text: str):
        super().__init__()
        self.type = ButtonTypes.KEYBOARD
        self.text = f"{text}{self._JOIN_SYMBOL}"


class InlineKeyButton(Button):
    _JOIN_SYMBOL = "|"

    def __init__(self, module_name: str, text: str, callback_data: str, url=None):
        super().__init__()
        self.type = ButtonTypes.INLINE
        self.text = text
        self.callback_data = f"{module_name}{self._JOIN_SYMBOL}{callback_data}"
        self.url = url
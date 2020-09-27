#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from telegos.helpers.dict_helper import DictSerialize


class BaseModel(DictSerialize):
    def __init__(self):
        super().__init__()

    def from_tg(self, data):
        class_vars = self.__dict__
        for var in class_vars:
            if var.startswith("_"):
                continue

            if atr := getattr(data, var):
                if var in self._dict_handlers:
                    model = self._dict_handlers[var]()
                    model.from_tg(atr)
                    atr = model.to_dict()
                setattr(self, var, atr)

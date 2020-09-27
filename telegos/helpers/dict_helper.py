#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictSerialize:
    def __init__(self):
        self._dict_handlers = {}

    def from_dict(self, dict_data: dict):
        keys = self.__dict__.keys()
        for key, value in dict_data.items():
            if key in keys:
                if key in self._dict_handlers and isinstance(value, dict):
                    obj = self._dict_handlers[key]()
                    obj.from_dict(value)
                    value = obj
                setattr(self, key, value)

    def to_dict(self, pass_null=True, pass_internal_attr=True):
        result = {}
        for var in self.__dict__:
            if pass_internal_attr and var.startswith("_"):
                continue

            var_val = self.__dict__[var]
            if not pass_null:
                result[var] = self.__dict__[var]
                continue

            if var_val:
                if var in self._dict_handlers:
                    var_val = var_val.to_dict()

                result[var] = var_val
        return result
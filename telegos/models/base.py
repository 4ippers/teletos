#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class BaseModel:
    def to_json(self, pass_null=True, pass_internal_attr=True) -> str:
        result = self.to_dict(pass_null, pass_internal_attr)
        return json.dumps(result)

    def from_tg(self, data):
        class_vars = self.__dict__
        for var in class_vars:
            if atr := getattr(data, var):
                setattr(self, var, atr)

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





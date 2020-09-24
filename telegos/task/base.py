#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random


def generate_task_id() -> str:
    return str(random.randint(0, 100000))


class BaseTask:
    def __init__(self):
        self.id = generate_task_id()
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

    def to_json(self, pass_null=True, pass_internal_attr=True):
        attrs = self.to_dict(pass_null, pass_internal_attr)
        return json.dumps(attrs)
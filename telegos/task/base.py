#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
from telegos.helpers.dict_helper import DictSerialize


def generate_task_id() -> str:
    return str(random.randint(0, 100000))


class BaseTask(DictSerialize):
    def __init__(self):
        super().__init__()
        self.id = generate_task_id()
        self.type = None

    def to_json(self, pass_null=True, pass_internal_attr=True):
        attrs = self.to_dict(pass_null, pass_internal_attr)
        return json.dumps(attrs)
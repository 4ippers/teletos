#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegos.models.base import BaseModel


class UserModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.id = None
        self.full_name = None
        self.username = None
        self.is_bot = False

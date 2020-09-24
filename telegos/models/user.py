#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import BaseModel


class UserModel(BaseModel):
    def __init__(self):
        self.id = None
        self.full_name = None
        self.username = None
        self.is_bot = False

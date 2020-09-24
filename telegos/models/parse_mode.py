#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ParseMode:
    MARKDOWN = 'Markdown'
    MARKDOWN_V2 = 'MarkdownV2'
    HTML = 'HTML'

    @staticmethod
    def is_valid_parse_mode(parse_mode: str) -> bool:
        self_vars_values = vars(ParseMode).values()
        if parse_mode in self_vars_values:
            return True
        return False
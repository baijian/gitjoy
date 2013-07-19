# -*- coding: utf-8 -*-

import string
import random
from datetime import datetime
import markdown2

def get_current_time():
    return datetime.now()

def markdown_to_html(content):
    return markdown2.markdown(content)

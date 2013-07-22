# -*- coding: utf-8 -*-

import string
import random
from datetime import datetime
import markdown2

def get_current_time():
    return datetime.now()

def markdown_to_html(content):
    return markdown2.markdown(content)

def get_github_client_id():
    return "f019301fecbfa5ef6f33"

def get_github_client_secret():
    return "ebc8cb90d1becc14448fb9ee4c3a0065fe2754fa"

def get_github_oauth_address():
    return "https://github.com/login/oauth/authorize"

def get_github_redirect_uri():
    return "http://git.joinjoy.me:5000/login"

def get_github_token_address():
    return "https://github.com/login/oauth/access_token"


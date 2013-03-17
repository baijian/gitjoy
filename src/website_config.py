# -*- coding: utf-8 -*-
from os.path import dirname,abspath

CUR_DIR = dirname(abspath(__file__))
#print CUR_DIR

#Config
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 1
PRODUCTION_CONIFG = CUR_DIR + '/../website_config.py'

#Session
SECRET_KEY = r"42a3e1376f8852d1c0620a3235886bcd712879a4"

#DB
SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:123456@localhost/demo'

#Log
ERROR_LOG = CUR_DIR + '/../logs/flask.error.log'
ERROR_LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'

#APP
BLOB_PATH = '/tmp'

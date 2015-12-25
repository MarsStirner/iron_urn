# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from tsukino_usagi.client import TsukinoUsagiClient

__author__ = 'viruzzz-kun'


app = Flask(__name__)

db = SQLAlchemy()


class MyUsagi(TsukinoUsagiClient):
    def on_configuration(self, configuration):
        app.config.update(configuration)
        db.init_app(app)


usagi = MyUsagi(
    app.wsgi_app,
    os.getenv('TSUKINO_USAGI_URL'),
    os.getenv('TSUKINO_USAGI_SUBSYSTEM')
)
app.wsgi_app = usagi.app
usagi()

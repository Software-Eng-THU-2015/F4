# -*- coding: utf-8 -*-
import web
import os

class Body:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    
    def GET(self):
        return self.render.reply_body()
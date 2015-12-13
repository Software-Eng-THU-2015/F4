# -*- coding: utf-8 -*-
import web
import os
import database
import datetime

class Plan:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):

    	row = web.input()
        openid = row.openid

        #在数据库中查询用户运动数据
        

        return self.render.reply_plan(openid)

    def POST(self):

        data = web.input()
        openid = data.openid
        height = data.get("height")
        weight = data.get("weight")
        calories = data.get("calories")

        try:
            x = int(height)
        except:
            return self.render.reply_myplan("身高数据错误", "", "")
        try:
            y = int(weight)
        except:
            return self.render.reply_myplan("体重数据错误", "", "")
        try:
            z = int(calories)
        except:
            return self.render.reply_myplan("目标数据错误", "", "")
        

        old_plan = self.db.plan.get(openid)
        if old_plan:
            self.db.plan.update(openid=openid, height=x, weight=y, goal_calo=z)
        else:
            self.db.plan.insert(openid=openid, height=x, weight=y, goal_calo=z)

        return self.render.reply_myplan("您的身高：%d" %x,"您的体重：%d" %y,"您的目标：%d" %z)

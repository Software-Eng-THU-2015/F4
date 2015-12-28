# coding: UTF-8
import os
 
import web
 
from weixinInterface import WeixinInterface
from sport import Sport
from sleep import Sleep
from body import Body
from follower import Follower
from info import Info
from confirm import Confirm
from rank import Rank
from plan import Plan
from pk import Pk
from fight import Fight
from weapon import Weapon
from banish import Banish

urls = (
'/weixin','WeixinInterface',
'/sport', 'Sport',
'/sleep', 'Sleep',
'/body', 'Body',
'/follower', 'Follower',
'/info', 'Info',
'/confirm', 'Confirm',
'/rank', 'Rank',
'/plan', 'Plan',
'/pk', 'Pk',
'/fight', 'Fight',
'/weapon', 'Weapon',
'/banish', 'Banish'
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

def notfound():
	return web.notfound(render.notfound())

def internalerror():
	return web.internalerror(render.internalerror())

app = web.application(urls, globals())
app.notfound = notfound
app.internalerror = internalerror
application = app.wsgifunc()
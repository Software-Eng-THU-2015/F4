# -*- coding: utf-8 -*-
import httplib
import database

class tool:
	def __init__(self):
		self.db = database.database()
		self.accessToken = self.db.message.get_token()
		self.appId = self.db.message.get_appid()
		self.appSecret = self.db.message.get_appsecret()

		self.BASEURL = "api.weixin.qq.com"
		self.TOKENURL = "/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (self.appId, self.appSecret)
		self.USERURL = "/cgi-bin/user/info?access_token=%s&openid=%s&lang=zh_CN"		

	def refresh_token(self):
		#更新token
		conn = httplib.HTTPSConnection(self.BASEURL)
		conn.request("GET", self.TOKENURL)
		tokenJson = eval(conn.getresponse().read())
		self.accessToken = tokenJson["access_token"]
		self.db.message.update_token(self.accessToken)
		conn.close()

	def get_user_msg(self, userOpenId):	
		#获取用户信息，如nickname
		conn = httplib.HTTPSConnection(self.BASEURL)
		conn.request("GET", self.USERURL % (self.accessToken, userOpenId))
		try:
			userInfoJson = eval(conn.getresponse().read())
			conn.close()
			if "errcode" in userInfoJson:
				if userInfoJson["errcode"] == 42001 or userInfoJson["errcode"] == 40001:
					self.refresh_token()
					conn = httplib.HTTPSConnection(self.BASEURL)
					conn.request("GET", self.USERURL % (self.accessToken, userOpenId))
					userInfoJson = eval(conn.getresponse().read())
					conn.close()

			if "nickname" in userInfoJson:
				return userInfoJson
		except:
			pass
		return {}
# -*- coding: utf-8 -*-
import web
import sae
import datetime
import httplib

class database:
	def __init__(self):
		self.db = web.database(
				dbn="mysql",  
				db=sae.const.MYSQL_DB,  
				user=sae.const.MYSQL_USER,  
				pw=sae.const.MYSQL_PASS,  
				host=sae.const.MYSQL_HOST,  
				port=int(sae.const.MYSQL_PORT),  
			)
	
		self.message = message(self.db)
		self.user = user(self.db)
		self.bong = bong(self.db)
		self.follower = follower(self.db)
		self.stranger = stranger(self.db)
		self.weapon = weapon(self.db)
		self.plan = plan(self.db)

class message:
	def __init__(self, db):
		self.db = db

	def get_token(self):
		try:
			reply = self.db.query("select * from Message where Type = 'TOKEN'")[0].Text
		except:
			reply = ""
		return reply

	def get_appid(self):
		try:
			reply = self.db.query("select * from Message where Type = 'APPID'")[0].Text
		except:
			reply = ""
		return reply

	def get_appsecret(self):
		try:
			reply = self.db.query("select * from Message where Type = 'APPSECRET'")[0].Text
		except:
			reply = ""
		return reply

	def update_token(self, accessToken):
		return self.db.update("Message", where = "id = 1", Text = accessToken)

class user:
	def __init__(self, db):
		self.db = db

	def insert(self, openid, uname = "anonymous", headimgurl = "http://fb.topit.me/b/3c/6c/11480604151c06c3cbl.jpg"):
		return self.db.insert("User", Uname = uname, OpenID = openid, ImageUrl = headimgurl)

	def delete(self, openid):
		return self.db.delete("User", where = "OpenID = $id", vars = {"id": openid, })

	def update(self, openid, uname = "", headimgurl = ""):
		if uname and headimgurl:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Uname = uname, ImageUrl = headimgurl)
		if uname:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Uname = uname)
		if headimgurl:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, ImageUrl = headimgurl)
		return -1

	def get(self, openid = "", id = ""):
		if not (openid or id):
			return {}
		try:
			if openid:
				user = self.db.query("select * from User where OpenID = $id", vars = {"id": openid, })[0]
			elif id:
				user = self.db.query("select * from User where id = $id", vars = {"id": id, })[0]
			userdic = {}
			userdic["openid"] = user.OpenID
			userdic["id"] = user.id
			userdic["nickname"] = user.Uname
			userdic["headimgurl"] = user.ImageUrl
			userdic["point"] = user.Point
			userdic["total_point"] = user.TotalPoint
			userdic["signin_time"] = user.SignInTime
		except:
			userdic = {}
		return userdic

	def sign_in(self, openid):
		return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, SignInTime = datetime.datetime.now().strftime("%Y-%m-%d %X"))

	def update_point(self, openid, new_point = -1, new_total_point = -1):
		if new_point >= 0 and new_total_point >= 0:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Point = new_point, TotalPoint = new_total_point)
		elif new_point >= 0:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Point = new_point)
		elif new_total_point >= 0:
			return self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, TotalPoint = new_total_point)
		else:
			return -1
		
class bong:
	def __init__(self, db):
		self.db = db
		self.data_type_1 = ["openid", "startTime", "endTime", "type", "subType"]
		self.data_type_2 = ["distance", "speed", "calories", "steps", "actTime", "nonActTime", "dsNum", "lsNum", "wakeNum", "wakeTimes", "score"]

		self.DATAURL = "wrist.ssast2015.com"
		self.TIMEURL = "/bongdata/?startTime=%s&endTime=%s&user=%d"

	def get_data(self, date_1, date_2, id):
		#从样例数据库获取数据
		conn = httplib.HTTPConnection(self.DATAURL)
		conn.request("GET", self.TIMEURL % (date_1, date_2, id))
		try:
			data = eval(conn.getresponse().read())
		except:
			data = {}
		conn.close()
		return data		

	'''def insert(self, openid, start_time, end_time, type, subtype, distance = 0, speed = 0, calories = 0, steps = 0, acttime = 0, nonacttime = 0, dsnum = 0, lsnum = 0, wakenum = 0, waketimes = 0, score = 0):
		if type not in range(1, 4):
			return -1
		if subtype not in range(1, 7):
			return -1
		return self.db.insert("Bong", 
			OpenID = openid, 
			StartTime = start_time, 
			EndTime = end_time, 
			Type = type, 
			SubType = subtype, 
			Distance = distance, 
			Speed = speed, 
			Calories = calories, 
			Steps = steps, 
			ActTime = acttime, 
			NonActTime = nonacttime, 
			DsNum = dsnum, 
			LsNum = lsnum, 
			WakeNum = wakenum, 
			WakeTimes = waketimes, 
			Score = score)'''

	def insert(self, data):
		for index in self.data_type_1:
			if index not in data:
				return -1
		if data["type"] not in range(1, 4):
			return -1
		if data["subType"] not in range(1, 7):
			return -1
		for index in self.data_type_2:
			if index not in data:
				data[index] = 0
		return self.db.insert("Bong", 
			OpenID = data["openid"], 
			StartTime = data["startTime"], 
			EndTime = data["endTime"], 
			Type = data["type"], 
			SubType = data["subType"], 
			Distance = data["distance"], 
			Speed = data["speed"], 
			Calories = data["calories"], 
			Steps = data["steps"], 
			ActTime = data["actTime"], 
			NonActTime = data["nonActTime"], 
			DsNum = data["dsNum"], 
			LsNum = data["lsNum"], 
			WakeNum = data["wakeNum"], 
			WakeTimes = data["wakeTimes"], 
			Score = data["score"])

	def delete(self, openid):
		return self.db.delete("Bong", where = "OpenID = $id", vars = {"id": openid, })

	def update(self):
		pass

	def get_calories(self, openid, date):
		date_1 = date + " 00:00:00"
		date_2 = datetime.datetime.strptime(date_1, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days = 1)
		date_2 = date_2.strftime("%Y-%m-%d %H:%M:%S")

		list = self.db.query("select * from Bong where StartTime >= $date_1 and StartTime < $date_2", vars = {"date_1": date_1, "date_2": date_2, })

		#try:
		#	id = self.db.query("select * from User where id = $id", vars = {"id": id, })[0]["id"] % 100
		#	list = self.get_data(date_1, date_2, id)
		#expect:
		#	return 0

		calories = 0
		try:
			for index in list:
				calories += index.Calories
		except:
			calories = 0
		return calories

	def get_sleep(self, openid, date):
		date_2 = date + " 14:00:00"
		date_1 = datetime.datetime.strptime(date_2, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days = 1)
		date_1 = date_1.strftime("%Y-%m-%d %H:%M:%S")
		
		list = self.db.query("select * from Bong where StartTime >= $date_1 and StartTime < $date_2 and Type = 1", vars = {"date_1": date_1, "date_2": date_2, })

		#try:
		#	id = self.db.query("select * from User where id = $id", vars = {"id": id, })[0]["id"] % 100
		#	list = self.get_data(date_1, date_2, id)
		#expect:
		#	return {"dsleep": 0, "lsleep": 0}
		
		dsleep = 0
		lsleep = 0
		try:
			for index in list:
				dsleep += index.DsNum
				lsleep += index.LsNum
		except:
			dsleep = 0
			lsleep = 0
		return {"dsleep": dsleep, "lsleep": lsleep}

class follower:
	def __init__(self, db):
		self.db = db

	def insert(self, follower_a, follower_b):
		reply_a = self.db.insert("Follower", FollowerID = follower_a, FollowingID = follower_b)
		reply_b = self.db.insert("Follower", FollowerID = follower_b, FollowingID = follower_a)
		return reply_a and reply_b

	def delete(self, follower):
		reply_a = self.db.delete("Follower", where = "FollowerID = $id", vars = {"id": follower, })
		reply_b = self.db.delete("Follower", where = "FollowingID = $id", vars = {"id": follower, })
		return reply_a and reply_b

	def update(self):
		pass

	def get(self, follower):
		follower_list = self.db.query("select * from Follower where FollowerID = $id", vars = {"id": follower, })
		reply_list = []
		for index in follower_list:
			reply = index.FollowingID
			reply_list.append(reply)
		return reply_list

	def is_followed(self, follower_a, follower_b):
		reply = self.db.query("select * from Follower where FollowerID = $id_a and FollowingID = $id_b", vars = {"id_a": follower_a, "id_b": follower_b})
		try:
			tmp = reply[0]
			return 1
		except:
			return 0

class stranger:
	def __init__(self, db):
		self.db = db

	def insert(self, to_user, from_user):
		return self.db.insert("Stranger", ToUserID = to_user, FromUserID = from_user)

	def delete(self, to_user = 0, from_user = 0, user = 0):
		if user:
			reply_a = self.db.delete("Stranger", where = "ToUserID = $id", vars = {"id": user, })
			reply_b = self.db.delete("Stranger", where = "FromUserID = $id", vars = {"id": user, })
			return reply_a and reply_b
		else:
			return self.db.delete("Stranger", where = "ToUserID = $id_a and FromUserID = $id_b", vars = {"id_a": to_user, "id_b": from_user, })

	def update(self):
		pass

	def get(self, to_user):
		stranger_list = self.db.query("select * from Stranger where ToUserID = $id", vars = {"id": to_user, })
		reply_list = []
		for index in stranger_list:
			reply = index.FromUserID
			reply_list.append(reply)
		return reply_list


class weapon:
	def __init__(self, db):
		self.db = db

	def insert(self, openid, weaponcode):
		if weaponcode <= 0:
			return -1
		weapon_list = self.db.query("select * from Weapon where OpenID = $id and WeaponCode = $wpcode", vars = {"id": openid, "wpcode": weaponcode, })
		try:
			tmp = weapon_list[0]
			return -1
		except:
			return self.db.insert("Weapon", OpenID = openid, WeaponCode = weaponcode)

	def delete(self, openid):
		return self.db.delete("Weapon", where = "OpenID = $id", vars = {"id": openid, })

	def update(self, openid, old_weaponcode, new_weaponcode):
		if new_weaponcode < 0:
			return -1
		return self.db.update("Weapon", where = "OpenID = $id and WeaponCode = $wpcode", vars = {"id": openid, "wpcode": old_weaponcode, }, WeaponCode = new_weaponcode)

	def get(self, openid):
		weapon_list = self.db.query("select * from Weapon where OpenID = $id", vars = {"id": openid, })
		reply_list = []
		for index in weapon_list:
			reply = index.WeaponCode
			reply_list.append(reply)
		return reply_list

class plan:
	def __init__(self, db):
		self.db = db

	def insert(self, openid, height, weight, goal_calo):
		if height < 0 or weight < 0 or goal_calo < 0:
			return -1
		plan_list = self.db.query("select * from Plan where OpenID = $id", vars = {"id": openid, })
		try:
			tmp = plan_list[0]
			return self.db.update("Plan", where = "OpenID = $id", vars = {"id": openid, }, Height = height, Weight = weight, GoalCalo = goal_calo)
		except:
			return self.db.insert("Plan", OpenID = openid, Height = height, Weight = weight, GoalCalo = goal_calo)

	def delete(self, openid):
		return self.db.delete("Plan", where = "OpenID = $id", vars = {"id": openid, })

	def update(self, openid, height = -1, weight = -1, goal_calo = -1):
		tmp_plan = self.get(openid)
		if not tmp_plan:
			return -1
		if height < 0:
			height = tmp_plan["height"]
		if weight < 0:
			weight = tmp_plan["weight"]
		if goal_calo < 0:
			goal_calo = tmp_plan["goal_calo"]

		return self.db.update("Plan", where = "OpenID = $id", vars = {"id": openid, }, Height = height, Weight = weight, GoalCalo = goal_calo)

	def get(self, openid):
		plandic = {}
		try:
			plan = self.db.query("select * from Plan where OpenID = $id", vars = {"id": openid, })[0]
			plandic["openid"] = plan.OpenID
			plandic["height"] = plan.Height
			plandic["weight"] = plan.Weight
			plandic["goal_calo"] = plan.GoalCalo
		except:
			plandic = {}
		return plandic
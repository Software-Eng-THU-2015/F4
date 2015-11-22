import web
import sae

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
		self.sport = sport(self.db)

class message:
	def __init__(self, db):
		self.db = db

	def get_token(self):
		return self.db.query("select * from Message where Type = 'TOKEN'")[0].Text

	def get_appid(self):
		return self.db.query("select * from Message where Type = 'APPID'")[0].Text

	def get_appsecret(self):
		return self.db.query("select * from Message where Type = 'APPSECRET'")[0].Text

	def update_token(self, accessToken):
		if not accessToken:
			return 0
		self.db.update("Message", where = "id = 1", Token = accessToken)
		return 1

class user:
	def __init__(self, db):
		self.db = db

	def insert(self, uname, openid, imgurl):
		if not openid:
			return 0

		if not uname:
			uname = "anonymous"
		if not imgurl:
			imgurl = "http://fb.topit.me/b/3c/6c/11480604151c06c3cbl.jpg"

		self.db.insert('User', Uname = uname, OpenID = openid, ImageUrl = imgurl)
		return 1

	def delete(self, openid):
		if not openid:
			return 0
		self.db.delete("User", where = "OpenID = $id", vars = {"id": openid, })
		return 1

	def update(self, openid, uname, imgurl):
		if uname and imgurl:
			self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Uname = uname, ImageUrl = imgurl)
			return
		if uname:
			self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, Uname = uname)
			return
		if imgurl:
			self.db.update("User", where = "OpenID = $id", vars = {"id": openid, }, ImageUrl = imgurl)
			return

	def get(self, openid):
		if not openid:
			return 0
		return self.db.query("select * from User where OpenID = $id", vars = {"id": openid, })[0]

class sport:
	def __init__(self, db):
		self.db = db

	def insert(self):
		pass

	def delete(self):
		pass

	def update(self):
		pass

	def get(self, openid):
		if not openid:
			return 0
		return self.db.query("select * from Sport where UserID = $id", vars = {"id": openid, })
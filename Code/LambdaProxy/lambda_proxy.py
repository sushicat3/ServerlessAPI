import json
import sys
import os

sys.path.append('./lib')
import psycopg2

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='musicbrainz.cw2va02rdk2z.us-east-1.rds.amazonaws.com' password='musicbrainz' port='5432'")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			print('cannot connect to database')

	def get_users(self):
		select_command = 'select * from users'
		self.cursor.execute(select_command)
		users = self.cursor.fetchall()
		users_json = {}
		users_json['users'] = []
		for user in users:
			user_json = {}
			user_json['user_id'] = user[0]
			user_json['username'] = user[1]
			user_json['created_on'] = str(user[2])
			users_json['users'].append(user_json)
		
		return users_json

	def add_user(self, username):
		insert_command = "insert into users (username, created_on) values ('" + username + "', current_timestamp);"
		
		try:
			self.cursor.execute(insert_command)
			return self.cursor.statusmessage
		except psycopg2.Error as e:
			return e.pgerror

	def get_posts(self):
		select_command = 'select * from posts'
		self.cursor.execute(select_command)
		posts = self.cursor.fetchall()
		posts_json = {}
		posts_json['posts'] = []
		for post in posts:
			post_json = {}
			post_json['post_id'] = post[0]
			post_json['post'] = post[1]
			post_json['created_on'] = str(post[2])
			post_json['user_id'] = post[3]
			posts_json['posts'].append(post_json)
		
		return posts_json

	def get_posts_by_id(self, id):
		select_command = 'select * from posts where post_id =' + id 
		self.cursor.execute(select_command)
		post = self.cursor.fetchone()
		post_json = {}
		post_json['post_id'] = post[0]
		post_json['post'] = post[1]
		post_json['created_on'] = str(post[2])
		post_json['user_id'] = post[3]
		
		return post_json

	def get_posts_by_user_id(self, id):
		select_command = 'select * from posts where user_id =' + id 
		self.cursor.execute(select_command)
		posts = self.cursor.fetchall()
		posts_json = {}
		posts_json['posts'] = []
		for post in posts:
			post_json = {}
			post_json['post_id'] = post[0]
			post_json['post'] = post[1]
			post_json['created_on'] = str(post[2])
			post_json['user_id'] = post[3]
			posts_json['posts'].append(post_json)
		
		return posts_json

	def add_post(self, post, user_id):
		insert_command = "insert into posts (post, created_on, user_id) values ('" + post + "', current_timestamp, " + str(user_id) + ");"
		
		try:
			self.cursor.execute(insert_command)
			return self.cursor.statusmessage
		except psycopg2.Error as e:
			return e.pgerror
			
		

def request_handler(event, context):
	response = {}
	response['isBase64Encoded'] = False
	response['statusCode'] = 200

	headers = {'Content-Type': 'application/json'}
	response['headers'] = headers
	
	data_conn = DatabaseConnection()

	resources = event['pathParameters']['proxy'].split('/')
	method = event['httpMethod']
	if resources[0] == 'users':
		if method == 'GET':
			response['body'] = json.dumps(data_conn.get_users())
		elif method == 'POST':
			username = event['queryStringParameters']['username']
			response['body'] = json.dumps(data_conn.add_user(username))
		else:
			response['body'] = "Resource does not exist"
	elif resources[0] == 'posts':
		if method == 'GET':
			if (len(resources) == 1):
				response['body'] = json.dumps(data_conn.get_posts())
			elif (len(resources) == 2):
				response['body'] = json.dumps(data_conn.get_posts_by_id(resources[1]))
			else:
				response['body'] = json.dumps(data_conn.get_posts_by_user_id(resources[2]))
		elif method == 'POST':
			body = json.loads(event['body'])
			post = body['post']
			user_id = body['user_id']
			response['body'] = json.dumps(data_conn.add_post(post, user_id))
		else:
			response['body'] = "Resource does not exist"
	else:
		response['body'] = "Resource does not exist"

	return response
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

	def get(self):
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
			
		

def request_handler(event, context):
	response = {}
	response['isBase64Encoded'] = False
	response['statusCode'] = 200

	headers = {'Content-Type': 'application/json'}
	response['headers'] = headers
	
	data_conn = DatabaseConnection()
	response['body'] = json.dumps(data_conn.get())

	return response
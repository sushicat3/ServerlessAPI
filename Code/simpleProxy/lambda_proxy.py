import json
import sys
import os

POSTS = {
    'posts' : [
        {
            'user_id': 4,
            'post': 't provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.',
            'post_id': 7,
            'created_on': '2018-09-20 18:26:22.346810'
        },
        {
            'user_id': 2,
            'post': 'PostgreSQL has updatable views and materialized views, triggers, foreign keys; supports functions and stored procedures, and other expandability.',
            'post_id': 3,
            'created_on': '2018-09-19 16:48:53.619999'
        },
        {
            'user_id': 2,
            'post': 'PostgreSQL is ACID-compliant and transactional.',
            'post_id': 2,
            'created_on': '2018-09-19 16:48:40.341539'
        },
        {
            'user_id': 4,
            'post': 'GitHub Inc. is a web-based hosting service for version control using Git.',
            'post_id': 4,
            'created_on': '2018-09-20 18:25:06.280772'
        },
        {
            'user_id': 4,
            'post': 'It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.',
            'post_id': 6,
            'created_on': '2018-09-20 18:26:08.321004'
        },
        {
            'user_id': 2,
            'post': 'PostgreSQL, often simply Postgres, is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards compliance.',
            'post_id': 1,
            'created_on': '2018-09-19 16:45:50.884902'
        },
        {
            'user_id': 4,
            'post': 'It is mostly used for computer code.',
            'post_id': 5,
            'created_on': '2018-09-20 18:25:50.262681'
        }
    ]
}

USERS = {
    "users": [
        {
            "user_id": 3,
            "username": "pentapus",
            "created_on": "2018-09-19 22:17:12.017551"
        },
        {
            "user_id": 2,
            "username": "sushicat",
            "created_on": "2018-09-19 16:40:47.982052"
        },
        {
            "user_id": 4,
            "username": "octocat",
            "created_on": "2018-09-20 17:55:53.748842"
        },
        {
            "user_id": 5,
            "username": "happyphant",
            "created_on": "2018-09-20 17:58:34.812905"
        }
    ]
}

def get_users():
	return USERS

def get_posts():
	return POSTS


def request_handler(event, context):
	response = {}
	response['isBase64Encoded'] = False
	response['statusCode'] = 200

	headers = {'Content-Type': 'application/json'}
	response['headers'] = headers
	

	resources = event['pathParameters']['proxy'].split('/')
	method = event['httpMethod']
	if resources[0] == 'users':
		if method == 'GET':
			response['body'] = json.dumps(get_users())
		else:
			response['body'] = "Resource does not exist"
	elif resources[0] == 'posts':
		if method == 'GET':
			if (len(resources) == 1):
				response['body'] = json.dumps(get_posts())
		else:
			response['body'] = "Resource does not exist"
	else:
		response['body'] = "Resource does not exist"

	return response
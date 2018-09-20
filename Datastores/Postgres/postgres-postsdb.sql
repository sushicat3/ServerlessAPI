CREATE TABLE users(
 user_id serial PRIMARY KEY,
 username VARCHAR (50) UNIQUE NOT NULL,
 created_on TIMESTAMP NOT NULL
);

CREATE TABLE posts
(
  post_id serial PRIMARY KEY,
  post VARCHAR (280) NOT NULL,
  created_on TIMESTAMP NOT NULL,
  user_id integer REFERENCES users
);

INSERT INTO users (username, created_on)
VALUES
 ('sushicat', current_timestamp);

INSERT INTO posts (post, created_on, user_id)
VALUES
 ('PostgreSQL, often simply Postgres, is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards compliance.', current_timestamp, 2);


INSERT INTO posts (post, created_on, user_id)
VALUES
 ('PostgreSQL is ACID-compliant and transactional.', current_timestamp, 2);


INSERT INTO posts (post, created_on, user_id)
VALUES
 ('PostgreSQL has updatable views and materialized views, triggers, foreign keys; supports functions and stored procedures, and other expandability.', current_timestamp, 2);

INSERT INTO users (username, created_on)
VALUES
 ('pentapus', current_timestamp);


-- users added with api
	-- octocat
	-- happyphant

-- posts added with api for octocat
	-- GitHub Inc. is a web-based hosting service for version control using Git.
	-- It is mostly used for computer code.
	-- It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.
	-- It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.
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




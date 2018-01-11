CREATE TABLE apirelease( buildtime date, version varchar(30) primary key, links varchar2(30), methods varchar2(30));
Insert into apirelease values ('2017-01-01 10:00:00', "v1", "/api/v1/users", "get, post, put, delete");

CREATE TABLE users(username varchar2(30), email varchar2(30), password varchar2(30), full_name varchar(30), id integer primary key autoincrement);
Insert into users values ('user1', 'user1@users.com', 'user1', 'User 1', 1);
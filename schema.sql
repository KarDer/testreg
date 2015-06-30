drop table if exists user;
create table user (
  id integer primary key autoincrement,
  username string not null,
  email string not null UNIQUE,
  pass string not null,
  date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  phone integer not null,
  more string not null
);
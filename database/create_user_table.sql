drop table if exists tb_user;
create table tb_user (
  user_id integer primary key autoincrement,
  email string not null,
  password string not null,
  company_join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);


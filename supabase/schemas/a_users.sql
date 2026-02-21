-- describes users (name, email)
create table "users" (
  "id" uuid primary key not null,
  "name" text not null,
  "email" text unique not null,
  "mbti" text
);
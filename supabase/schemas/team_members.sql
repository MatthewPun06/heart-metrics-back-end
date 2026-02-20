-- relational table between teams and users
create table "team_members" (
  "team_id" uuid references teams(id) on delete cascade,
  "user_id" uuid references users(id) on delete cascade,
  "manager" boolean not null default false,
  "role" text not null
);
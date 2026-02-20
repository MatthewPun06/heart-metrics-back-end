-- stores calendar events for each user
create table "calendar_events" (
  "id" uuid primary key default uuid_generate_v4(),
  "user_id" uuid references users(id) on delete cascade,
  
  "title" text not null,
  "start_time" timestamp not null,
  "end_time" timestamp not null
);
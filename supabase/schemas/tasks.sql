-- stores tasks for each user
create table "tasks" (
  "id" uuid primary key default uuid_generate_v4(),
  "user_id" uuid references users(id) on delete cascade,
  
  "assignment_name" text not null,
  "description" text,
  "due_date" date
);
-- table storing user integrations with external services (e.g. calendar, task management)
create table "integrations" (
  "id" uuid primary key default uuid_generate_v4(),
  "user_id" uuid references users(id) on delete cascade,
  
  "service" text not null, -- e.g. "google_calendar", "asana"
  "access_token" text not null, -- token for accessing the external service's API
  "refresh_token" text, -- token for refreshing the access token if needed
  "expires_at" timestamp -- when the access token expires
);
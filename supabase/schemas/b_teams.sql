-- describes teams (name, health metrics)
create table "teams" (
  "id" uuid primary key default uuid_generate_v4(),
  "name" text not null,

  -- information about the team health
  "wwi" integer,
  "protection_from_harm" integer,
  "connection_and_community" integer,
  "opportunity_for_growth" integer,
  "mattering_at_work" integer,
  "work_life_harmony" integer,

  -- information about the last survey
  "last_survey_date" timestamp,
  "time_between_surveys" integer -- in days
);
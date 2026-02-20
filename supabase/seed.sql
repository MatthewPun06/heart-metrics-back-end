insert into "users" 
    (name, email) 
values 
    ('John Doe', 'john.doe@example.com'),
    ('Jane Smith', 'jane.smith@example.com')


-- insert into "tasks"
--     (user_id, assignment_name, description, due_date)
-- values
--     ((select id from users where email = 'john.doe@example.com'), 'Finish project report', 'Complete the final report for the project', '2024-07-01'),


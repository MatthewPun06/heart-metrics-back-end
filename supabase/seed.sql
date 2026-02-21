insert into users 
    (name, email) 
values 
    ('john doe', 'john.doe@example.com'),
    ('jane smith', 'jane.smith@example.com'),
    ('alice johnson', 'alice.johnson@example.com'),
    ('bob brown', 'bob.brown@example.com');

insert into tasks
    (user_id, assignment_name, description) 
values 
    ((select id from users where email = 'john.doe@example.com'), 'Task 1', 'Description for Task 1'),
    ((select id from users where email = 'jane.smith@example.com'), 'Task 2', 'Description for Task 2');



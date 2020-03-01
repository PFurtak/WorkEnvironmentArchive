CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(75),
    email VARCHAR(100),
    username VARCHAR(30),
    password VARCHAR(100),
    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
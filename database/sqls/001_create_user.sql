CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL UNIQUE
);
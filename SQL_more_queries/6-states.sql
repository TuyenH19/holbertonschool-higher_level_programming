-- Create database and table in that database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

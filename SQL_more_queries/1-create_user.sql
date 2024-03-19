-- Create the MySQL server user and set password
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON mysql.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

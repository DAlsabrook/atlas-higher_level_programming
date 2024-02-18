-- Creates new user and grants all permissions to the user
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NULL;
GRANT ALL TO 'user_0d_1'@'localhost':
FLUSH PRIVILEGES;

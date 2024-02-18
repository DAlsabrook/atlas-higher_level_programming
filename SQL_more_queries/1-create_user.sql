-- Creates new user and grants all permissions to the user
CREATE USER "user_0d_1"@"localhost" IDENTIFIED BY "user_0d_1_pwd" IF NULL;
GRANT ALL ON hbtn_0c_0.* TO "user_0d_1"@"localhost":
FLUSH PRIVILEGES;

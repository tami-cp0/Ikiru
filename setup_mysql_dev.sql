-- prepares a MySQL server for the project
-- this is just a temporary setup
-- i also hard coded the details when creating the engine

-- if they say the password does not meet password requirement, use this command to check your policy
-- SHOW VARIABLES LIKE 'validate_password.policy';
-- then add "SET GLOBAL validate_password.policy=LOW;" to line 12
-- then add "SET GLOBAL validate_password.policy=<YOUR_POLICY>;" TO line 14

DROP DATABASE IF EXISTS ikiru_dev_db;
CREATE DATABASE IF NOT EXISTS ikiru_dev_db;

CREATE USER IF NOT EXISTS 'ikiru_user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL ON `ikiru_dev_db`.* TO 'ikiru_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ikiru_user'@'localhost';
FLUSH PRIVILEGES;

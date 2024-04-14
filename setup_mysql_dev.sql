-- prepares a MySQL server for the project

DROP DATABASE IF EXISTS ikiru_dev_db;

CREATE DATABASE IF NOT EXISTS ikiru_dev_db;

CREATE USER IF NOT EXISTS 'ikiru_user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL ON `ikiru_dev_db`.* TO 'ikiru_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ikiru_user'@'localhost';
FLUSH PRIVILEGES;

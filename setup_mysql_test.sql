-- This script that prepares a MySQL server for the project,
-- it uses the hbnb_test_db database, create a new user called
-- hbnb_dev (in localhost), it set the password of hbnb_dev to
-- hbnb_dev_pwd, asign all privileges to the database and select
-- privilege to the database performance_schema.

CREATE database IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
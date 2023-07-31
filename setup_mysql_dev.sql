-- This script that prepares a MySQL server for the project,
-- it uses the hbnb_dev_db database, create a new user called
-- hbnb_dev (in localhost), it set the password of hbnb_dev to
-- hbnb_dev_pwd, asign all privileges to the database and select
-- privilege to the database performance_schema.

CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
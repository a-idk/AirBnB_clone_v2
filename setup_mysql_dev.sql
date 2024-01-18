--   To create an MySQL server using:
--   Database = hbnb_dev_db
--   User = hbnb_dev
--   password = hbnb_dev_pwd
--   hbnb_test should have all privileges on the database hbnb_test_db
--   hbnb_test should have SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;

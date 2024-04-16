-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create read-only user
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost"
               IDENTIFIED BY "hbnb_dev_pwd";

-- grant "select" privilege
GRANT SELECT
   ON performance_schema.*
   TO "hbnb_dev"@"localhost";

-- grant "select" privilege
GRANT ALL
   ON hbnb_dev_db.*
   TO "hbnb_dev"@"localhost";

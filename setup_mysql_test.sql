-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create read-only user
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost"
               IDENTIFIED BY "hbnb_test_pwd";

-- grant "select" privilege
GRANT SELECT
   ON performance_schema.*
   TO "hbnb_test"@"localhost";

-- grant "select" privilege
GRANT ALL
   ON hbnb_test_db.*
   TO "hbnb_test"@"localhost";

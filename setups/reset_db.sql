-- reset db
USE ikiru_db;

SET FOREIGN_KEY_CHECKS = 0;

-- Get the list of tables
SET group_concat_max_len = 2048;
SELECT GROUP_CONCAT(table_name) INTO @tables
FROM information_schema.tables
WHERE table_schema = DATABASE();

-- Create the DROP TABLE command
SET @drop_tables_query = CONCAT('DROP TABLE IF EXISTS ', @tables);

-- Prepare and execute the DROP TABLE command
PREPARE stmt FROM @drop_tables_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET FOREIGN_KEY_CHECKS = 1;
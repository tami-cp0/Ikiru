-- Set the database name
USE ikiru_db;

-- Query to get all table names
SET group_concat_max_len = 2048;
SELECT GROUP_CONCAT(table_name) INTO @tables_to_drop
FROM information_schema.tables
WHERE table_schema = DATABASE();

-- Construct DROP TABLE statement
SET @drop_tables_query = CONCAT('DROP TABLE IF EXISTS ', COALESCE(@tables_to_drop, 'dummy_table'));

-- Execute DROP TABLE statement
PREPARE drop_tables_statement FROM @drop_tables_query;
EXECUTE drop_tables_statement;
DEALLOCATE PREPARE drop_tables_statement;

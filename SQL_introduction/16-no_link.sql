-- script to list all records of the table and ignore rows with no name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
SQL_introduction/15-groups.sql SQL_introduction/16-no_link.sql

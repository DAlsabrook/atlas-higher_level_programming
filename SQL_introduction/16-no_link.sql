-- script to list all records of the table and ignore rows with no name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

-- List all cities of California that are in the database
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states AS states
    WHERE states.name = 'California'
)
ORDER BY id ASC;

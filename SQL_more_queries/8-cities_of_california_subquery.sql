-- List all cities of California that are in the database
SELECT cities.id, cities.name
FROM cities AS city
WHERE city.state_id = (
    SELECT states.id
    FROM states AS states
    WHERE states.name = 'California'
)
ORDER BY city.id ASC;

-- list all cities in database
SELECT cities.id, cities.name, states.name
FROM
    cities
JOIN
    states
ORDER BY
    cities.id ASC;

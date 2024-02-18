-- list all cities in database
SELECT cities.id, cities.name, states.name
FROM
    hbtn_0d_usa.cities
JOIN
    hbtn_0d_usa.states
ORDER BY
    cities.id ASC;

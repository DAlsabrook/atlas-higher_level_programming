-- list all cities in database
SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states ON states.id=cities.state_id;

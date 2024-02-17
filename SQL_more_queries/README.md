
![Guy in server room](https://github.com/DAlsabrook/atlas-higher_level_programming/assets/112190470/b7834329-1e2d-4d8e-a601-54f59bac99e3)

# SQL More Queries

## Directory Overview
The SQL_advanced_queries directory encompasses a collection of SQL scripts tailored for managing user permissions, handling data integrity, and querying complex relationships within a database focused on geographical and entertainment data. This suite of scripts is designed for users with an intermediate to advanced understanding of SQL, providing tools for sophisticated data manipulation and analysis.

Here’s a brief overview of what each script category aims to achieve:

User Management and Permissions: Scripts numbered from 0-privileges to 2-create_read_user focus on the foundational aspects of database security by creating users, defining their access levels, and ensuring that data can be securely read without unauthorized modifications.

Data Integrity and Constraints: Files 3-force_name through 5-unique_id are dedicated to ensuring the integrity of the data stored within the database. These scripts implement various constraints to prevent invalid data entry and ensure uniqueness where necessary.

Geographical Data Handling: The series from 6-states to 9-cities_by_state_join dives into managing and querying geographical data, including states and cities, with an emphasis on relational data management techniques such as JOINs and subqueries.

Entertainment Database Queries: Starting from 10-genre_id_by_show to 16-shows_by_genre, these scripts explore the entertainment domain, focusing on managing and analyzing data related to shows and genres. They include operations for categorizing shows, counting entries by category, and filtering data based on specific criteria like genre.

This directory serves as a practical resource for SQL practitioners looking to expand their skills in database management, querying complex relationships, and ensuring data security and integrity. Whether you’re managing user access, enforcing data standards, or analyzing relational data, the SQL_advanced_queries directory provides a comprehensive toolkit for sophisticated database operations.

## Files Description

- [0-privileges](0-privileges.sql) - Sets up or modifies user permissions within the database system, allowing for control over who can access and manipulate data.
- [1-create_user](1-create_user.sql) - Creates a new user account in the database system, specifying login credentials and potentially assigning initial roles or privileges.
- [2-create_read_user](2-create_read_user.sql) - Establishes a new user with permissions limited to reading data from the database, ensuring secure access without the ability to modify data.
- [3-force_name](3-force_name.sql) - Implements constraints to ensure that a 'name' field in a specified table is always provided and meets certain criteria.
- [4-never_empty](4-never_empty.sql) - Applies constraints or checks to guarantee that certain fields in a database table cannot be left empty.
- [5-unique_id](5-unique_id.sql) - Ensures that the 'id' column in a table remains unique for each record, possibly setting up a primary key or unique constraint.
- [6-states](6-states.sql) - Creates or queries a table listing states, potentially including operations to insert, update, or list state data.
- [7-cities](7-cities.sql) - Similar to the 'states' script but focused on cities, this file likely involves creating or querying a table of city information.
- [8-cities_of_california_subquery](8-cities_of_california_subquery.sql) - Utilizes a subquery to retrieve a list of cities located in California, demonstrating nested queries.
- [9-cities_by_state_join](9-cities_by_state_join.sql) - Employs JOIN operations to match cities with their respective states, showcasing relational database querying techniques.
- [10-genre_id_by_show](10-genre_id_by_show.sql) - Retrieves the genre IDs associated with specific shows, illustrating the use of foreign keys or relational joins.
- [11-genre_id_all_shows](11-genre_id_all_shows.sql) - Queries the database for the genre IDs of all shows, potentially for a comprehensive mapping of shows to genres.
- [12-no_genre](12-no_genre.sql) - Identifies shows that have not been assigned a genre, which could be useful for database cleaning or updating.
- [13-count_shows_by_genre](13-count_shows_by_genre.sql) - Counts the number of shows within each genre, providing insights into the distribution of show types.
- [14-my_genres](14-my_genres.sql) - Likely a personalized query that retrieves genres of interest to the user or genres related to specific criteria.
- [15-comedy_only](15-comedy_only.sql) - Filters the database to return only shows classified under the comedy genre, exemplifying targeted querying.
- [16-shows_by_genre](16-shows_by_genre.sql) - Organizes shows by their genre, possibly using grouping or sorting SQL operations to enhance data retrieval.

## Getting Started

To dive into these advanced SQL scripts, ensure that your SQL server is up and running. Open your preferred SQL management tool, connect to your server, and start executing the scripts in sequence. This will help you progressively understand and apply complex SQL features and techniques in real-world scenarios.

## Author

[David Alsabrook](https://github.com/DAlsabrook)

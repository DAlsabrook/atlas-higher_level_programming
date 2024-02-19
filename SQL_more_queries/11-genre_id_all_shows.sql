-- Shows all shows in database
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, 'NULL')
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC

-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name as genre,
        COUNT(tv_shows.id) as number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id AND tv_shows.title IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

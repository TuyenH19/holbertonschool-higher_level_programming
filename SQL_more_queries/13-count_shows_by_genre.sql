-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_show_genres.name as genre, COUNT(tv_show_genres.genre_id) as number_of_shows
FROM tv_genres
    LEFT JOIN tv_show_genres 
    ON tv_genres.id = tv_show_genres.show_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
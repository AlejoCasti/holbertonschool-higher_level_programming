-- Scriptat that display number of
SELECT tg.name AS genre,
COUNT(tsg.show_id) AS number_of_shows
FROM tv_show_genres AS tsg
LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
GROUP BY tg.name
ORDER BY number_of_shows DESC;

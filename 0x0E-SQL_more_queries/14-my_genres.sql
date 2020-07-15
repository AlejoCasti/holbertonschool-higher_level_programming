-- script that lists all genres 
SELECT tg.name
FROM tv_show_genres AS tsg
INNER JOIN tv_shows AS ts
ON tsg.show_id = ts.id
INNER JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE ts.title = "Dexter"
ORDER BY tg.name ASC;

-- script thta lists all Comedy shows
SELECT ts.title, tg.name
FROM tv_show_genres AS tsg
RIGHT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
RIGHT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
ORDER BY ts.title ASC,
tg.name ASC;

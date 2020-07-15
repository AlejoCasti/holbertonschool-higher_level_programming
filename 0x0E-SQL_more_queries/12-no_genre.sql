-- Script that found no genre
SELECT ts.title, tsg.genre_id
FROM tv_show_genres AS tsg
RIGHT JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title ASC,
tsg.genre_id;

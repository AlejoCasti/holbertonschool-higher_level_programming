-- Write a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT ts.title, tsg.genre_id FROM tv_show_genres AS tsg
RIGHT JOIN tv_shows AS ts ON tsg.show_id = ts.id
ORDER BY ts.title ASC, tsg.genre_id;

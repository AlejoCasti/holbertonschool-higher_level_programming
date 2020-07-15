-- script that lsits all cities on california
SELECT id, name FROM cities WHERE state_id = 
(SELECT id FROM states WHERE name = 'california') ORDER BY id;

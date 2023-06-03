-- script that lists all records with a score >= 10
-- scores ordered by score (top first)
SELECT `name`, `score`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

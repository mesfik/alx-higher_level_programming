-- script that lists all records with a score >= 10
-- Records are ordered by descending score.
SELECT `name`, `score`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

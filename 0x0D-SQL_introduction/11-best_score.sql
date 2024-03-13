-- lists the best score
-- using command
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

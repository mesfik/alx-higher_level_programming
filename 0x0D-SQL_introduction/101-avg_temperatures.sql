-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temperatures) AS avg_temp
FROM temperatures
ORDER BY temperatures DESC;

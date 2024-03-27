USE hbtn_0c_0;
SELECT city, AVG(temp) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

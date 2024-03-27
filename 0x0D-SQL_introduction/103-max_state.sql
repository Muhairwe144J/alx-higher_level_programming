USE hbtn_0c_0;
SELECT state, MAX(temp) AS max_temp FROM temperatures GROUP BY state ORDER BY state;

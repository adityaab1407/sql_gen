SELECT 
    s1.id AS id,
    s1.name AS name,
    s1.age AS age,
    s1.city AS city,
    s1.salary AS salary_source1,
    s2.department AS department,
    s2.position AS position,
    s2.salary AS salary_source2
FROM 
    source1 s1
LEFT JOIN 
    source2 s2
ON 
    s1.id = s2.id;

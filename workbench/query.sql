SELECT df1.id, df1.name, df1.age, df2.department, df2.position
FROM df1
LEFT JOIN df2 ON df1.id = df2.id

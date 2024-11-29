# sql_gen
The SQL Generator with Workspace Analysis is an intelligent web application that automates SQL query creation by analyzing the structure of your SQL workspace. Leveraging AI, the application generates SQL queries based on user input and the detected schema, provides detailed explanations, and allows execution of these queries on your database.

Features
1. Workspace Analysis
Automatically scans your SQL workspace directory to:
Detect all SQL files.
Extract table structures, column names, and relationships (e.g., primary keys, foreign keys).
Map your database schema into an internal representation.
2. AI-Powered SQL Query Generation
Uses a Large Language Model (LLM) to:
Understand your input (e.g., "Find the total sales by region").
Draft SQL queries tailored to your workspace schema.
Suggest optimized queries based on detected relationships.
3. Query Execution
Executes approved SQL queries on your connected database.
Supports popular database systems like MySQL, PostgreSQL, SQLite, etc.
4. Interactive Results
Provides a detailed explanation of the generated SQL query.
Displays a preview of the query results.
Allows exporting results as a CSV file.
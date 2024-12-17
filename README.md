# sql_gen
The SQL Generator with Workspace Analysis is an intelligent companion that automates SQL query creation by analyzing the structure of your workspace. The LLM model generates SQL queries based on user input and the detected schema and allows execution of these queries on your database.

## Features

### 1. Workspace Analysis
Automatically scans your SQL workspace directory to:
- Detect all SQL files.
- Extract table structures and column names
- Map your database schema into an internal representation.

### 2. AI-Powered SQL Query Generation
Uses a Large Language Model (LLM) to:
- Understand your input (e.g., "Find the total sales by region").
- Draft SQL queries tailored to your workspace schema.
- Suggest optimized queries based on detected relationships.

### 3. Query Execution
- Executes approved SQL queries on your csv files
- Supports popular database systems like MySQL, PostgreSQL, SQLite, etc. (Future Enhancement)

### 4. Interactive Results
- Provides a detailed explanation of the generated SQL query.
- Displays a preview of the query results.
- Allows exporting results as a CSV file in your workspace.
- After generating a SQL query, the application automatically saves the query to a `.sql` file in your workspace directory for future reference. The file is saved as `query.sql` in the specified workspace folder.

## Installation

1. Clone the repository.
2. Install the required dependencies.

```bash
pip install -r requirements.txt

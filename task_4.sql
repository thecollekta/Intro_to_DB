-- Task 4: Print full description of the table 'books'

-- Use alx_book_store database
USE alx_book_store;

-- Select column information from the information_schema.columns table
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'Books'
    AND TABLE_SCHEMA = 'alx_book_store';
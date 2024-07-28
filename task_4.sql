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
FROM information_schema.columns
WHERE
    table_name = 'books'
    AND table_schema = 'alx_book_store';
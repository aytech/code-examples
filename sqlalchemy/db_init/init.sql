CREATE TABLE IF NOT EXISTS public.test (
    age INT,
    name VARCHAR(20),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
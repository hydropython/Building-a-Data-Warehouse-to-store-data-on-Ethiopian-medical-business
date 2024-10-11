{{ config(materialized='table') }}

WITH processed_data AS (
    SELECT
        id,
        CASE
            WHEN message ~ '^[A-Za-z ]+' THEN  -- Checks if the message starts with letters (product name)
                TRIM(SUBSTRING(message FROM '^(.*?)\s+'))  -- Extracts product name until the first space
            ELSE NULL
        END AS product_name,
        CASE
            WHEN message ~ '\s[0-9]+\s?[A-Za-z]*' THEN  -- Checks if a number followed by text (optional) appears in the message
                TRIM(SUBSTRING(message FROM '\s([0-9]+\s?[A-Za-z]*)'))  -- Extracts the number and possible text after
            ELSE NULL
        END AS usage_info,
        date
    FROM {{ ref('telegram_data_source') }}
)

SELECT 
    id,
    product_name,
    usage_info,
    date
FROM processed_data
WHERE product_name IS NOT NULL OR usage_info IS NOT NULL
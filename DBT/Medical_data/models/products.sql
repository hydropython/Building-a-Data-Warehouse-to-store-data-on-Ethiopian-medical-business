-- models/products.sql

{{ config(materialized='table') }}

SELECT DISTINCT
    product_name
FROM {{ ref('transform_telegram_data') }}
WHERE product_name IS NOT NULL
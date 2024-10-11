-- models/usage.sql

{{ config(materialized='table') }}

SELECT DISTINCT
    usage_info
FROM {{ ref('transform_telegram_data') }}
WHERE usage_info IS NOT NULL
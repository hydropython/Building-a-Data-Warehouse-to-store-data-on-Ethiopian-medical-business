{{ config(materialized='table') }}

SELECT *
FROM "telegram_data_Doctors_Ethiopia"
WHERE "Message" IS NOT NULL
{{ config(materialized='table') }}

SELECT "Channel Title", "Channel Username", "ID", "Message", "Date", "Media Path"
FROM "telegram_data_Doctors_Ethiopia"
WHERE "Message" IS NOT NULL
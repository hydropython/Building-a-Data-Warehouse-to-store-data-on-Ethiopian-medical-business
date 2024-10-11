* Telegram Data Transformation DBT Project
---
This project transforms Telegram messages for Lobelia4Cosmetics, extracting relevant product and usage information from the raw dataset using DBT (Data Build Tool).

Project Overview
---

This DBT project processes Telegram messages, focusing on:

Product Extraction: Identifying product names based on the message structure.
Usage Information: Extracting numerical usage data when it appears in the message.

Key SQL Transformations
---

Product Identification: Extracts product names from messages that begin with letters.
Usage Information Extraction: Labels messages that end with numbers as usage information.
ID Integration: Ensures each product and usage data is associated with its respective id for reference.
The project is designed to read from a raw Telegram data source (telegram_data_source), process the messages, and create two tables: one for products and one for usage, with the respective IDs.

Requirements
---

To work with this DBT project, ensure you have the following dependencies:

DBT version 1.8.7 or higher
A Postgres database (adjust your configuration in dbt_project.yml accordingly)
Git for version control

Getting Started
---

1. Clone the Repository
To get started, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/telegram_data_dbt.git
cd telegram_data_dbt

2. Install DBT
If you haven't installed DBT yet, follow the instructions below:

bash
Copy code
pip install dbt-postgres

3. Configure the Database Connection
Update your profiles.yml file to connect to your database. Here is an example for a Postgres setup:

yaml
Copy code
your_profile_name:
  outputs:
    dev:
      type: postgres
      host: your-database-host
      user: your-username
      password: your-password
      port: 5432
      dbname: your-database-name
      schema: public
  target: dev

4. Run the Models
After setting up the DBT project and configuring your database connection, run the DBT models to generate the transformed tables:

bash
Copy code
dbt run
This command will create the following models:

telegram_data_source: The raw table containing Telegram data.
transform_telegram_data: The processed data with extracted product and usage information.
products: Table containing products with their corresponding IDs.
usage: Table containing usage information with their corresponding IDs.

5. Test and Validate
To ensure everything is set up correctly, you can run tests:

bash
Copy code
dbt test
This will validate the correctness of the transformations.

Project Structure
---

models/: Contains the DBT models (SQL transformations).
telegram_data_source.sql: Raw data extraction model.
transform_telegram_data.sql: Main transformation script that processes and extracts product and usage data from messages.
products.sql: Processes products extracted from the raw data.
usage.sql: Processes usage data extracted from the raw data.
dbt_project.yml: Configuration file for the DBT project.

Troubleshooting
---
Error: Node not found: Ensure that the model names in your SQL scripts match exactly with those in your DBT configurations.
Database Connection Issues: Verify that your profiles.yml contains the correct credentials and database host information.

License
---
This project is licensed under the MIT License. See the LICENSE file for details.
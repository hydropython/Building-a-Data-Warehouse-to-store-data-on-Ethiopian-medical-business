import unittest
import pandas as pd
import os
from io import StringIO
from your_module import clean_telegram_data  # Make sure to adjust this import based on your module location

class TestCleanTelegramData(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV data to use as input
        self.sample_data = StringIO("""
        Channel Title,Channel Username,Message,Date,Media Path,Extra Column
        My Channel,channel1,Hello World,2022-10-01 12:00:00,/path/to/media,
        My Channel,channel1,Hello World,2022-10-01 12:00:00,/path/to/media,
        Another Channel,channel2,Test Message,2023-01-15 08:30:00,,/path/to/media2
        Another Channel,,Missing Username,2023-03-25 10:20:00,/path/to/media3,
        My Channel,channel1,Hello Future,2025-01-01 12:00:00,/path/to/media4,
        """)
        self.input_file_path = "test_input.csv"
        self.output_file_path = "test_output.csv"
        
        # Save the sample data to a test CSV file
        with open(self.input_file_path, 'w') as f:
            f.write(self.sample_data.getvalue())

    def tearDown(self):
        # Remove the test CSV files after each test
        if os.path.exists(self.input_file_path):
            os.remove(self.input_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_cleaning_process(self):
        # Call the clean_telegram_data function
        clean_telegram_data(self.input_file_path, self.output_file_path)
        
        # Load the output data
        cleaned_df = pd.read_csv(self.output_file_path)
        
        # Test: Check if the required columns are present
        expected_columns = ["Channel Title", "Channel Username", "Message", "Date", "Media Path"]
        self.assertListEqual(list(cleaned_df.columns), expected_columns, "Required columns are missing or incorrect")
        
        # Test: Check if duplicates were removed
        self.assertEqual(len(cleaned_df), 3, "Duplicate rows were not removed correctly")
        
        # Test: Check if missing values were dropped
        self.assertFalse(cleaned_df.isnull().values.any(), "Not all missing values were handled correctly")
        
        # Test: Check if future dates were removed
        future_dates = cleaned_df[cleaned_df['Date'] > pd.Timestamp.now(tz='UTC')]
        self.assertEqual(len(future_dates), 0, "Future dates were not removed")

    def test_date_format(self):
        # Call the clean_telegram_data function
        clean_telegram_data(self.input_file_path, self.output_file_path)
        
        # Load the output data
        cleaned_df = pd.read_csv(self.output_file_path)

        # Test: Check if 'Date' is in datetime format
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned_df['Date']), "Date column is not in datetime format")

if __name__ == '__main__':
    unittest.main()
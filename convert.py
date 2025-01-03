import pandas as pd
import json

json_file_path = "data\chat_translation.json"

# Read the JSON file and ensure proper handling of Turkish characters
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame with the required columns
df = pd.DataFrame(data)[["gpt_en", "gpt_tr"]]

# Save the DataFrame to a CSV file with correct encoding for Turkish characters
csv_file_path = "data/gpt_translations_corrected.csv"
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

csv_file_path
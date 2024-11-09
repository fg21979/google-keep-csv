#!/usr/bin/env python3
# coding: utf-8

import os
import json
import csv
from glob import glob
from datetime import datetime

# Define output CSV file
now = datetime.now()
csvout = f"notes_{now.strftime('%Y-%m-%d_%H%M')}.csv"

# Write headers and extract data from JSON files
with open(csvout, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["title", "textContent", "labels", "attachments"])

    # Loop through each JSON file in the directory
    for file in glob("Keep/**/*.json", recursive=True):
        with open(file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

            # Extract fields with defaults if they are missing
            title = data.get("title", "")
            text_content = data.get("textContent", "")

            # Process labels to create a comma-separated string
            labels = ', '.join([label['name'] for label in data.get("labels", [])])

            # Process attachments to create a comma-separated list of attachment paths
            attachments = ', '.join([attachment['filePath'] for attachment in data.get("attachments", [])])

            # Write the row to CSV
            writer.writerow([title, text_content, labels, attachments])

print(f"Done! Notes saved to {csvout}")

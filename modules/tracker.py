import csv
from datetime import datetime
import os

def log_application(job_data, resume):
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    file_path = "data/applications.csv"

    # If file doesn't exist, write headers
    write_header = not os.path.exists(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["title", "company", "location", "date_applied", "resume"])
        writer.writerow([
            job_data.get("title", ""),
            job_data.get("company", ""),
            job_data.get("location", ""),
            datetime.now().isoformat(),
            resume
        ])

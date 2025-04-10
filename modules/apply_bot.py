def apply_to_job(job):
    print(f"Auto-applying to: {job['title']} at {job['company']}")

# === modules/tracker.py ===
import csv
from datetime import datetime

def log_application(job_data, resume):
    with open("data/applications.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            job_data["title"], job_data["company"], job_data["location"],
            datetime.now().isoformat(), resume
        ])

"""
Assignment 5 - Milestone 5: Maintain Listening History and Handle Bad Data
Course: Python Programming (COM-501)
Course Outcome: CO5 | Bloom's Level: 5

Debugging Note:
Fault: The malformed record 'Unknown Episode|Podcast|abc|6' contains non-numeric data
'abc' in the duration field (which triggers a ValueError during int('abc')) and an out-of-range
rating of 6 (valid rating range is 1.0 to 5.0).
Correction: The parsing and numeric conversions for each record are enclosed in an inner
try-except ValueError block inside the line-by-line reading loop. When a malformed record is
encountered, the error is caught and logged, allowing execution to proceed smoothly and process
all subsequent valid records without application crash. Furthermore, an outer try-except block
handles FileNotFoundError in the event that the file is not found.
"""

import os

# Path to persistent file
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "listening_history.txt")

# Sample write / append
with open(filename, "w", encoding="utf-8") as f:
    f.write("Track 1|Song|180|4.5\n")
    f.write("Unknown Episode|Podcast|abc|6\n")  # Malformed line
    f.write("Track 2|Song|240|4.9\n")

valid_records = []

try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f"Initial file position: {f.tell()}")
        for line in f:
            parts = line.strip().split("|")
            try:
                title, mtype, duration_str, rating_str = parts
                duration = int(duration_str)
                rating = float(rating_str)
                if not (1 <= rating <= 5):
                    raise ValueError("Rating out of bounds")
                valid_records.append((title, mtype, duration, rating))
            except ValueError as e:
                print(f"[LOG ERROR] Skipping malformed record '{line.strip()}': {e}")
except FileNotFoundError:
    print("History file not found.")

print(f"Successfully Loaded {len(valid_records)} Records:")
for record in valid_records:
    print(" - ", record)

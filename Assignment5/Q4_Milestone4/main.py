"""
main.py - Main execution script demonstrating modularization, dictionary mapping, and lambdas
Part of Assignment 5 - Milestone 4
Course: Python Programming (COM-501)
Course Outcome: CO4 | Bloom's Level: 4
"""

import time
from media_utils import seconds_to_hms, filter_by_rating, summarize_by_type

items = [
    {"title": "Song A", "type": "Song", "rating": 3.5, "duration": 210},
    {"title": "Song B", "type": "Song", "rating": 4.8, "duration": 180},
    {"title": "Podcast X", "type": "Podcast", "rating": 4.2, "duration": 3600}
]

start_t = time.time()

# Lambda sorting: sort items by rating descending
sorted_items = sorted(items, key=lambda x: x['rating'], reverse=True)

# Menu choices dictionary mapping functions
menu = {
    "1": lambda: filter_by_rating(items, 4.0),
    "2": lambda: summarize_by_type(items)
}

high_rated = menu["1"]()
type_summary = menu["2"]()
exec_time = time.time() - start_t

print(f"Filtered (Rating >= 4.0): {[i['title'] for i in high_rated]}")
print(f"Summary by Type: {type_summary}")
print(f"Formatted Total Time: {seconds_to_hms(sum(i['duration'] for i in items))}")
print(f"Analytics Generated in: {exec_time:.6f}s")

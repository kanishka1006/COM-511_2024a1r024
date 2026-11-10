"""
Assignment 5 - Milestone 2: Build a Multi-Item Listening Queue
Course: Python Programming (COM-501)
Course Outcome: CO2 | Bloom's Level: 4

Description:
Stores multiple media records in a list of dictionaries, validates input ranges,
tracks unique creators in a set, and categorizes duration into Quick, Standard,
or Long-form.
"""

queue = []
creators = set()
counts = {"Quick": 0, "Standard": 0, "Long-form": 0}

items_data = [
    ("Song A", "Artist 1", "SONG", 200, 4.2),
    ("Bad Item", "Artist 2", "SONG", -10, 6.0),  # invalid record (rejected)
    ("Talk Episode", "Speaker X", "PODCAST", 2000, 4.8)
]

for title, creator, mtype, duration, rating in items_data:
    if duration <= 0 or not (1 <= rating <= 5):
        print(f"[REJECTED] Invalid record: {title}")
        continue

    cat = "Quick" if duration <= 300 else ("Standard" if duration <= 1800 else "Long-form")
    counts[cat] += 1
    creators.add(creator)
    queue.append({
        "title": title,
        "creator": creator,
        "type": mtype,
        "duration": duration,
        "rating": rating,
        "category": cat
    })

total_time = sum(item["duration"] for item in queue)
highest_rated = max(queue, key=lambda x: x["rating"]) if queue else None

print(f"Total Listening Time: {total_time}s")
print(f"Unique Creators Count: {len(creators)}")
if highest_rated:
    print(f"Top Rated: {highest_rated['title']} ({highest_rated['rating']})")
print(f"Categories: {counts}")

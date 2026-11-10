"""
media_utils.py - Reusable utility module for media analytics
Part of Assignment 5 - Milestone 4
Course: Python Programming (COM-501)
Course Outcome: CO4 | Bloom's Level: 4
"""

def seconds_to_hms(seconds):
    """Convert duration in seconds to formatted hh:mm:ss string."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}h {m}m {s}s"


def filter_by_rating(items, min_rating=4.0):
    """Filter media items having rating greater than or equal to min_rating."""
    return [item for item in items if item['rating'] >= min_rating]


def summarize_by_type(items):
    """Count and summarize total items grouped by their media type."""
    summary = {}
    for item in items:
        media_type = item['type']
        summary[media_type] = summary.get(media_type, 0) + 1
    return summary
